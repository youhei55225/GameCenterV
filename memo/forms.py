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
        fields = ('title','body','my_char','opp_char')#,'tag')
        labels = {
            'title': 'タイトル',
            'body': '本文',
            'my_char': '自分のキャラクター',
            'opp_char': '相手のキャラクター'
            #'tag':'タグ'
        }
    CHOICE = {
        ('立ち回り','立ち回り'),
        ('コンボ','コンボ'),
        ('反撃','反撃'),
        ('その他','その他')
    }
    one = forms.ChoiceField(
        label='タグ',
        required=True,
        disabled=False,
        initial=['立ち回り'],
        choices=CHOICE,
        widget=forms.Select(attrs={
            'id': 'one',
        })
    )
        

class UpdateMemoForm(forms.ModelForm):
    class Meta:
        model = Memos
        fields = ('title','body')
        labels = {
            'title':'タイトル',
            'body':'本文'
        }

'''
class ChoiceTagForm(forms.Form):

    fields = ('tag')
    CHOICE = (
        ('footsies','立ち回り'),
        ('combo','コンボ'),
        ('punish','反撃'),
        ('others','その他')
    )
    select = forms.fields.ChoiceField(required=True,widget=forms.widgets.Select,choices=CHOICE)
'''