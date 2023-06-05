from django.urls import path
from app2.views import *
app_name='nothing'
urlpatterns=[
    path('app2_htmlpage/',app2_htmlpage,name='app1_htmlpage'),
]