from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def fbv_string(request):
    return HttpResponse('<h1> This is fbv_string </h1>')

def fbv_html(request):
    return render(request,'fbvstring.html')

class cbv_string(View):
    def get(self,request):
        return HttpResponse('<h1> This is cbv_string </h1>')

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html') 

