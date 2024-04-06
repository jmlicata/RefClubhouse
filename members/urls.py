from django.urls import path
from members import views

urlpatterns = [
    path('', views.index, name = 'home'),
    path('member', views.member_edit, name = 'member')
]