from django import forms
from . models import Memo,Memos


class MemoForm(forms.ModelForm):
    class Meta:
        model = Memo
        #fields = ('title','body', 'author', 'my_char','opp_char')
        fields = ('title','body','my_char','opp_char')
        labels = {
            'title': 'タイトル',
            'body': '本文',
            'my_char': '自分のキャラクター',
            'opp_char': '相手のキャラクター'
        }

class MemosForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ('title','body','my_char','opp_char')
        labels = {
            'title': 'タイトル',
            'body': '本文',
            'my_char': '自分のキャラクター',
            'opp_char': '相手のキャラクター'
        }

class UpdateMemoForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ('title','body')
        labels = {
            'title':'タイトル',
            'body':'本文'
        }

