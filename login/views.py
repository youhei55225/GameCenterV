from urllib import request
from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginForm, User, UserResisterForm
from django.views import generic

from django.contrib.auth import get_user_model,login
from django.contrib.auth.mixins import UserPassesTestMixin

from django.views.generic import CreateView
from django.http.response import HttpResponseRedirect

# Create your views here.

#def index(request):
#    params = {
#        'form' : LoginForm,
#    }
#    return render(request,'login/index.html',params)

#def top(request):
#    return render(request,'login/top.html')

def test(request):
    return render(request,'login/test.html')

class Login(LoginView):
    form_class = LoginForm
    template_name = 'login/index.html'

class TopView(generic.TemplateView):
    template_name = 'login/top.html'

class Logout(LogoutView):
    template_name = 'login/logout_done.html'

class OnlyYouMixin(UserPassesTestMixin):
    raise_exception = True

    def test_func(self):
        user = self.request.user
        return user.pk == self.kwargs['pk']

class MyPage(OnlyYouMixin, generic.DetailView):
    model = User
    template_name = 'login/my_page.html'

def UserResister(request):
    prms = {
        'form':UserResisterForm
    }
    return render(request,'login/user_resister.html',prms)
    

def UserResisterSuccess(request):
    if request.method == 'POST':
        User.objects.create_user(request.POST['username'],'',request.POST['password'])
    return render(request,'login/user_resister_success.html')