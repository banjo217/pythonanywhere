from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import logout as logout_user
from django.contrib.auth import authenticate
# Create your views here.
def index(req):
	#return HttpResponse('welcome' + req.method)
    return render(req,'myweb/index.html')

def login_active(req):
    if req.method =="POST":
        Username = req.POST.get("username")
        Password = req.POST.get("password")
        user = authenticate(username=Username, password=Password)
        if user is not None:
            login(req, user)
            return redirect('/index2')
    context = {}
    return render(req, 'myweb/login.html', context)
def logout(req):
    logout_user(req)
    return redirect('login')

def index2(request):
    return render(request,'myweb/index2.html')

def commady(request):
    return render(request,'myweb/commady.html')

def gintama(request):
    return render(request,'myweb/gintama.html')

def gintama1(request):
    return render(request,'myweb/gintama1.html')

def gintama2(request):
    return render(request,'myweb/gintama2.html')

def gintama3(request):
    return render(request,'myweb/gintama3.html')

def action(request):
    return render(request,'myweb/action.html')

def adventure(request):
    return render(request,'myweb/adventure.html')

def beelzebub(request):
    return render(request,'myweb/beelzebub.html')

def beelzebub1(request):
    return render(request,'myweb/beelzebub1.html')

def beelzebub2(request):
    return render(request,'myweb/beelzebub2.html')

def beelzebub3(request):
    return render

def Danshi(request):
    return render(request,'myweb/Danshi.html')

def Danshi1(request):
    return render(request,'myweb/Danshi1.html')

def Danshi2(request):
    return render(request,'myweb/Danshi2.html')

def Danshi3(request):
    return render(request,'myweb/Danshi3.html')

def day(request):
    return render(request,'myweb/day.html')

def day1(request):
    return render(request,'myweb/day1.html')

def day2(request):
    return render(request,'myweb/day2.html')

def day3(request):
    return render(request,'myweb/day3.html')

def doc(request):
    return render(request,'myweb/doc.html')

def doc1(request):
    return render(request,'myweb/doc1.html')

def doc2(request):
    return render(request,'myweb/doc2.html')

def doc3(request):
    return render(request,'myweb/doc3.html')

def doremon(request):
    return render(request,'myweb/doremon.html')

def doremon1(request):
    return render(request,'myweb/doremon1.html')

def doremon2(request):
    return render(request,'myweb/doremon2.html')

def doremon3(request):
    return render(request,'myweb/doremon3.html')

def fantasy(request):
    return render(request,'myweb/fantasy.html')

def fate(request):
    return render(request,'myweb/fate.html')

def fate1(request):
    return render(request,'myweb/fate1.html')

def fate2(request):
    return render(request,'myweb/fate2.html')

def fate3(request):
    return render(request,'myweb/fate3.html')

def ghoul(request):
    return render(request,'myweb/ghoul.html')

def ghoul1(request):
    return render(request,'myweb/ghoul1.html')

def ghoul2(request):
    return render(request,'myweb/ghoul2.html')

def ghoul3(request):
    return render(request,'myweb/ghoul3.html')

def log(request):
    return render(request,'myweb/log.html')

def log1(request):
    return render(request,'myweb/log1.html')

def log2(request):
    return render(request,'myweb/log2.html')

def log3(request):
    return render(request,'myweb/log3.html')

def oneman(request):
    return render(request,'myweb/oneman.html')

def oneman1(request):
    return render(request,'myweb/oneman1.html')

def oneman2(request):
    return render(request,'myweb/oneman2.html')

def oneman3(request):
    return render(request,'myweb/oneman3.html')

def onepiecestampede(request):
    return render(request,'myweb/onepiecestampede.html')

def onepiecestampede1(request):
    return render(request,'myweb/onepiecestampede1.html')

def onepiecestampede2(request):
    return render(request,'myweb/onepiecestampede2.html')

def onepiecestampede3(request):
    return render(request,'myweb/onepiecestampede3.html')

def sket(request):
    return render(request,'myweb/sket.html')

def sket1(request):
    return render(request,'myweb/sket1.html')

def sket2(request):
    return render(request,'myweb/sket2.html')

def sket3(request):
    return render(request,'myweb/sket3.html')

def slime(request):
    return render(request,'myweb/slime.html')

def slime1(request):
    return render(request,'myweb/slime1.html')

def slime2(request):
    return render(request,'myweb/slime2.html')

def slime3(request):
    return render(request,'myweb/slime3.html')

def themovie(request):
    return render(request,'myweb/themovie.html')

def yaiba(request):
    return render(request,'myweb/yaiba.html')

def yaiba1(request):
    return render(request,'myweb/yaiba1.html')

def yaiba2(request):
    return render(request,'myweb/yaiba2.html')

def yaiba3(request):
    return render(request,'myweb/yaiba3.html')

def yourname(request):
    return render(request,'myweb/yourname.html')

def yourname1(request):
    return render(request,'myweb/yourname1.html')

def yourname2(request):
    return render(request,'myweb/yourname2.html')

def yourname3(request):
    return render(request,'myweb/yourname3.html')
#def (request):
    #return render(request,'myweb/.html')