from django.urls import path
from . import views

urlpatterns = [
     #path('',views.index, name='index'),
     path('',views.Login.as_view(), name='index'),
     #path('top/',views.top, name='top'),
     path('top/',views.TopView.as_view(),name='top'),
     path('test/',views.test, name='test'),
     path('logout/',views.Logout.as_view(), name='logout'),
]
