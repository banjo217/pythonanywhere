from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(req):
	#return HttpResponse('welcome' + req.method)
    return render(req,'myweb/index.html')

def united(req):
    return render(req,'myweb/united.html')