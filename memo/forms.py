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
        fields = ('title','body')#,'my_char','opp_char')#,'tag')
        labels = {
            'title': 'タイトル',
            'body': '本文',
            #'my_char': '自分のキャラクター',
            #'opp_char': '相手のキャラクター'
            #'tag':'タグ'
        }
    CHOICE = (
        ('立ち回り','立ち回り'),
        ('コンボ','コンボ'),
        ('反撃','反撃'),
        ('その他','その他')
    )
    one = forms.ChoiceField(
        label='タグ',
        required=True,
        disabled=False,
        initial=['立ち回り'],
        choices=CHOICE,
        widget=forms.Select(attrs={
            'id': 'one',
        })
        # ↑の意味がよくわからん
    )

    CHOICECharacter = (
        ('指定しない','指定しない'),
        ('リュウ','リュウ'),
        ('春麗','春麗'),
        ('ナッシュ','ナッシュ'),
        ('ベガ','ベガ'),
        ('キャミィ','キャミィ'),
        ('バーディー','バーディー'),
        ('ケン','ケン'),
        ('ネカリ','ネカリ'),
        ('バルログ','バルログ'),
        ('レインボー・ミカ','レインボー・ミカ'),
        ('ラシード','ラシード'),
        ('かりん','かりん'),
        ('ザンギエフ','ザンギエフ'),
        ('ララ','ララ'),
        ('ダルシム','ダルシム'),
        ('ファン','ファン'),
        ('アレックス','アレックス'),
        ('ガイル','ガイル'),
        ('いぶき','いぶき'),
        ('バイソン','バイソン'),
        ('ジュリ','ジュリ'),
        ('ユリアン','ユリアン'),
        ('豪鬼','豪鬼'),
        ('コーリン','コーリン'),
        ('エド','エド'),
        ('アビゲイル','アビゲイル'),
        ('メナト','メナト'),
        ('是空','是空'),
        ('さくら','さくら'),
        ('ブランカ','ブランカ'),
        ('ファルケ','ファルケ'),
        ('コーディー','コーディー'),
        ('Ｇ','Ｇ'),
        ('サガット','サガット'),
        ('影ナル者','影ナル者'),
        ('ポイズン','ポイズン'),
        ('エドモンド本田','エドモンド本田'),
        ('ルシア','ルシア'),
        ('ギル','ギル'),
        ('セス','セス'),
        ('ダン','ダン'),
        ('ローズ','ローズ'),
        ('あきら','あきら'),
        ('オロ','オロ'),
        ('ルーク','ルーク')
    )
    ChoiceMyCharacter = forms.ChoiceField(
        label='自分のキャラクター',
        required=True,
        disabled=False,
        initial=['指定しない'],
        choices=CHOICECharacter,
        widget=forms.Select(attrs={
            'id': 'one',
        })
    )
    ChoiceOppCharacter = forms.ChoiceField(
        label='相手のキャラクター',
        required=True,
        disabled=False,
        initial=['指定しない'],
        choices=CHOICECharacter,
        widget=forms.Select(attrs={
            'id': 'one',
        })
    )



        
class CharctersSelectForm(forms.Form):
    CHOICE = (
        ('指定しない','指定しない'),
        ('リュウ','リュウ'),
        ('春麗','春麗'),
        ('ナッシュ','ナッシュ'),
        ('ベガ','ベガ'),
        ('キャミィ','キャミィ'),
        ('バーディー','バーディー'),
        ('ケン','ケン'),
        ('ネカリ','ネカリ'),
        ('バルログ','バルログ'),
        ('レインボー・ミカ','レインボー・ミカ'),
        ('ラシード','ラシード'),
        ('かりん','かりん'),
        ('ザンギエフ','ザンギエフ'),
        ('ララ','ララ'),
        ('ダルシム','ダルシム'),
        ('ファン','ファン'),
        ('アレックス','アレックス'),
        ('ガイル','ガイル'),
        ('いぶき','いぶき'),
        ('バイソン','バイソン'),
        ('ジュリ','ジュリ'),
        ('ユリアン','ユリアン'),
        ('豪鬼','豪鬼'),
        ('コーリン','コーリン'),
        ('エド','エド'),
        ('アビゲイル','アビゲイル'),
        ('メナト','メナト'),
        ('是空','是空'),
        ('さくら','さくら'),
        ('ブランカ','ブランカ'),
        ('ファルケ','ファルケ'),
        ('コーディー','コーディー'),
        ('Ｇ','Ｇ'),
        ('サガット','サガット'),
        ('影ナル者','影ナル者'),
        ('ポイズン','ポイズン'),
        ('エドモンド本田','エドモンド本田'),
        ('ルシア','ルシア'),
        ('ギル','ギル'),
        ('セス','セス'),
        ('ダン','ダン'),
        ('ローズ','ローズ'),
        ('あきら','あきら'),
        ('オロ','オロ'),
        ('ルーク','ルーク')
    )
    MyCharacter = forms.ChoiceField(
        label='自分のキャラクター',
        required=True,
        disabled=False,
        initial=['指定しない'],
        choices=CHOICE,
        widget=forms.Select(attrs={
            'id': 'one',
        })
        # ↑の意味がよくわからん
    )

    OppCharacter = forms.ChoiceField(
        label='相手のキャラクター',
        required=True,
        disabled=False,
        initial=['指定しない'],
        choices=CHOICE,
        widget=forms.Select(attrs={
            'id': 'one',
        })
        # ↑の意味がよくわからん
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