from django.shortcuts import render

# Create your views here.
def app2_htmlpage(request):
    return render(request,'app2_htmlpage.html')
