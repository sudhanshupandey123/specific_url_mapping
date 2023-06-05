from django.urls import path
from app1.views import *
app_name='something'
urlpatterns=[
    path('app1_htmlpage/',app1_htmlpage,name='app1_htmlpage'),
    path('app1_string/',app1_string,name='app1_string'),
]