from django.shortcuts import render, redirect, get_object_or_404
from .models import Activity
from .forms import ActivityForm,SignUpForm
from django.contrib.auth import logout,authenticate,login as auth_login

from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponseRedirect("/login")

def table(request, day):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    acts = Activity.objects.all().filter(day=day, author_id=request.user.id).order_by('fromTime')
    return render(request,'tableapp/main.html',{'acts':acts,'day':day})

def make(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    if(request.method == "POST"):
        form = ActivityForm(request.POST)
        if form.is_valid():

            act = Activity()
            act.author = request.user
            act.content = form.data['content']
            act.day = form.data['day']
            act.fromTime = form.data['fromTime']
            act.toTime =form.data['toTime']
            # act.color = form.data['color']
            act.save()
            return redirect('index', day=act.day)
    else:
        form = ActivityForm
    return render(request, 'tableapp/make.html', {'form': form})

def delete(request, day, id):
    object = Activity.objects.get(id=id)
    object.delete()
    return HttpResponseRedirect('/table/'+day)



def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = SignUpForm(request.POST)
            if form.is_valid():
                form.save()
                username = form.data.get("username")
                raw_password = form.data.get("password1")
                user =  authenticate(username=username, password=raw_password)
                auth_login(request,user)
                return HttpResponseRedirect('/table/월요일')
        else:
            form = SignUpForm()
        return render(request, 'tableapp/signup.html', {'form': form})
    else:
        return HttpResponseRedirect('/table/월요일')

def login(request):
    if request.method == "POST":
        username = form.data["username"]
        password = form.data['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return HttpResponseRedirect('/table/월요일')
        else:
            return 'invalid login'



def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return HttpResponseRedirect('/')





