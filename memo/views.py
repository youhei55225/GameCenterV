from django.shortcuts import render
from .models import Memo
from .forms import MemoForm

# Create your views here.

def index(request):
    return render(request,'memo/index.html')

def top(request):
    return render(request,'memo/top.html')

def add_memo(request):
    params = {'form':MemoForm()}
    form = MemoForm(request.POST)
    if form.is_valid():
        tag = form.save(commit=False)
        tag.author = request.user
        tag.save()
    return render(request,'memo/add_memo.html',params)

def show_memos(request):
    if request.method == 'POST':
        prms = {
            'my_memos':Memo.objects.filter(author=request.user,my_char=request.POST['my_char'],opp_char=request.POST['opp_char'])
        }
        #print(request.POST.get("my_char"))
        return render(request,'memo/show_memos.html',prms)
    else:
        params = {
            'memos':Memo.objects.all(),
            'my_memos':Memo.objects.filter(author=request.user)
        }
        return render(request,'memo/show_memos.html',params)