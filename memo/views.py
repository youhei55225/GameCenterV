from django.shortcuts import render
from .models import Memo,Memos
from .forms import MemoForm,MemosForm,UpdateMemoForm
from django.views.generic import UpdateView

# Create your views here.

def index(request):
    return render(request,'memo/index.html')

def top(request):
    return render(request,'memo/top.html')

def add_memo(request):
    params = {'form':MemosForm()}
    form = MemosForm(request.POST)
    if form.is_valid():
        tag = form.save(commit=False)
        tag.author = request.user
        tag.save()
    return render(request,'memo/add_memo.html',params)

def show_memos(request):
    prms = {
        'memos':Memos.objects.all()
    }
    return render(request,'memo/show_memos.html',prms)

def memo_page(request):
    if request.method == 'GET':
        memo_id = int(request.GET['memo_id'])
        #print(type(memo_id))
        #print(memo_id)
        prms = {
            'the_memo':Memos.objects.get(pk=memo_id),
            'form':UpdateMemoForm(initial={
                'title':Memos.objects.get(pk=memo_id).title,
                'body':Memos.objects.get(pk=memo_id).body,
            })
        }
        return render(request,'memo/memo_page.html',prms)

    if request.method == 'POST':

        if request.POST.get('delete') == '削除':
            memo_id = int(request.GET['memo_id'])
            delete_memo = Memos.objects.get(pk=memo_id)
            delete_memo.delete()
            prms = {
               'my_memos':Memos.objects.filter(author=request.user)
            }
            return render(request,'memo/mymemos.html',prms)
        else:
            memo_id = int(request.GET['memo_id'])
            update_memo = Memos.objects.get(pk=memo_id)
            update_memo.title = request.POST['title']
            update_memo.body = request.POST['body']
            update_memo.save()
            prms = {
                'the_memo':Memos.objects.get(pk=memo_id),
                'form':UpdateMemoForm(initial={
                    'title':Memos.objects.get(pk=memo_id).title,
                    'body':Memos.objects.get(pk=memo_id).body,
                })
            }
            return render(request,'memo/memo_page.html',prms)

def edit_memo(request):
    return render(request,'memo/edit_memo.html')

def mymemos(request):
    prms = {
        'my_memos':Memos.objects.filter(author=request.user)
    }
    return render(request,'memo/mymemos.html',prms)

def evaluation_memo(request):
    if request.method == 'GET':
        memo_id = int(request.GET['memo_id'])
        eva_memo = Memos.objects.get(pk=memo_id)
        prms = {
            'eva_memo':eva_memo
        }
        return render(request,'memo/evaluation_memo.html',prms)
