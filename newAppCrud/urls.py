from django.urls import path
from .views import * 

app_name='newAppCrud'

urlpatterns=[
    path('',home,name='home'),
    path('create/',create,name='create')
]