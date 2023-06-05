from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app1_htmlpage(request):
    return render(request,'app1_htmlpage.html')
def app1_string(request):
    return HttpResponse('<marquee scrollamount="50px" bgcolor="chocolate"><h1>Welcome to Specific Url Mapping</h1></marquee>')

