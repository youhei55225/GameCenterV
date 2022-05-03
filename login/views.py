from django.shortcuts import render

from django.contrib.auth.views import LoginView, LogoutView
from .forms import LoginForm, User
from django.views import generic

from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import UserPassesTestMixin

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