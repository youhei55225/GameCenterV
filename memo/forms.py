from django import forms
from . models import Memo


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
