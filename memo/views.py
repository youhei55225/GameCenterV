from xml.dom.minidom import CharacterData
from django.shortcuts import render
from .models import Memo,Memos
from .forms import MemoForm,MemosForm,UpdateMemoForm,CharctersSelectForm
from django.views.generic import UpdateView

# Create your views here.

def index(request):
    return render(request,'memo/index.html')

def top(request):
    return render(request,'memo/top.html')

def add_memo(request):
    params = {
        'form':MemosForm()
        }
    form = MemosForm(request.POST)
    if form.is_valid():
        tag = form.save(commit=False)
        tag.author = request.user
        tag.tag = request.POST['one']
        tag.my_char = request.POST['ChoiceMyCharacter']
        tag.opp_char = request.POST['ChoiceOppCharacter']
        tag.save()
    return render(request,'memo/add_memo.html',params)

def show_memos(request):
    prms = {
        'memos':Memos.objects.all(),
        'characters' :CharctersSelectForm()
    }

    if request.method == 'POST':

        if request.POST['MyCharacter'] == '指定しない' and request.POST['OppCharacter'] == '指定しない':
            prms = {
                'memos':Memos.objects.all(),
                'characters':CharctersSelectForm()
            }
        elif request.POST['MyCharacter'] != '指定しない' and request.POST['OppCharacter'] == '指定しない':
            prms = {
                'memos':Memos.objects.filter(my_char=request.POST['MyCharacter']),
                'characters':CharctersSelectForm()
            }
        elif request.POST['MyCharacter'] == '指定しない' and request.POST['OppCharacter'] != '指定しない':
            prms = {
                'memos':Memos.objects.filter(opp_char=request.POST['OppCharacter']),
                'characters':CharctersSelectForm()
            }
        else:
            prms = {
                'memos':Memos.objects.filter(my_char=request.POST['MyCharacter'],opp_char=request.POST['OppCharacter']),
                'characters':CharctersSelectForm()
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
        'my_memos':Memos.objects.filter(author=request.user),
        'characters':CharctersSelectForm()
    }
    if request.method == 'POST':

        if request.POST['MyCharacter'] == '指定しない' and request.POST['OppCharacter'] == '指定しない':
            prms = {
                'my_memos':Memos.objects.filter(author=request.user),
                'characters':CharctersSelectForm()
            }
        elif request.POST['MyCharacter'] != '指定しない' and request.POST['OppCharacter'] == '指定しない':
            prms = {
                'my_memos':Memos.objects.filter(author=request.user,my_char=request.POST['MyCharacter']),
                'characters':CharctersSelectForm()
            }
        elif request.POST['MyCharacter'] == '指定しない' and request.POST['OppCharacter'] != '指定しない':
            prms = {
                'my_memos':Memos.objects.filter(author=request.user,opp_char=request.POST['OppCharacter']),
                'characters':CharctersSelectForm()
            }
        else:
            prms = {
                'my_memos':Memos.objects.filter(author=request.user,my_char=request.POST['MyCharacter'],opp_char=request.POST['OppCharacter']),
                'characters':CharctersSelectForm()
            }

    return render(request,'memo/mymemos.html',prms)

def memo_detail(request):
    if request.method == 'GET':
        memo_id = int(request.GET['memo_id'])
        the_memo = Memos.objects.get(pk=memo_id)
        prms = {
            'the_memo':the_memo
        }
        return render(request,'memo/memo_detail.html',prms)
