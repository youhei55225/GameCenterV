from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginForm(AuthenticationForm):

    #class Meta:
    #    model = User
    #    fields = ('username', 'password',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class UserResisterForm(forms.Form):
    
    username = forms.CharField(
        label = 'ユーザ名',
        max_length=200,
        required=True,
    )
    password = forms.CharField(
        label = 'パスワード',
        min_length=8,
        widget=forms.PasswordInput(),
    )

    

'''
class UserResisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = {
            'username',
            'password1',
            'password2',
        }
        labels = {
            'username':'ユーザ名',
            'password1':'パスワード',
            'password2':'確認用パスワード',
        }
'''