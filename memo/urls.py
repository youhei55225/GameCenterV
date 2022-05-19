from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
     path('',views.index, name='index'),
     path('top/',views.top, name='top'),
     path('add_memo/',views.add_memo, name='add_memo'),
     path('show_memos/',views.show_memos,name='show_memos')
]
