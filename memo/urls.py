from django.urls import path
from . import views

app_name = 'memo'

urlpatterns = [
     path('',views.index, name='index'),
     path('top/',views.top, name='top'),
     path('add_memo/',views.add_memo, name='add_memo'),
     path('show_memos/',views.show_memos,name='show_memos'),
     path('memo_page/',views.memo_page,name='memo_page'),
     path('edit_memo/',views.edit_memo,name='edit_memo'),
     path('mymemos/',views.mymemos,name='mymemos'),
     path('memo_detail/',views.memo_detail,name='memo_detail'),
]
