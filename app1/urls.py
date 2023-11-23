from django.urls import path
from app1.views import *
app_name='revv'
urlpatterns=[
  path('fun1/',fun1,name='fun1')
]