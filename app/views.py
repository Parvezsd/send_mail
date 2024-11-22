from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    EUFO=UserForms()
    EPFO=ProfileForms()
    d={'EUFO':EUFO,'EPFO':EPFO}
    if request.method=="POST" and request.FILES:
        NMUFDO=UserForms(request.POST)
        NMPFDO=ProfileForms(request.POST,request.FILES)
        if NMUFDO.is_valid() and NMPFDO.is_valid():
            
            MUFDO=NMUFDO.save(commit=False)
            pw=NMUFDO.cleaned_data['password']
            MUFDO.set_password(pw)
            MUFDO.save()

            MPFDO=NMPFDO.save(commit=False)
            MPFDO.username=MUFDO
            MPFDO.save()
            send_mail('Register',
            'Congratulations you applied successfully Saraswathi',
            'syedparvez5577@gmail.com',
            [MUFDO.email],
            fail_silently=False)


            return HttpResponse('REgistration is Successfull')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'register.html',d)

def home(request):
    if request.session.get('username'):
        username=request.session.get('username')
        d={'username':username}
        return render(request,'home.html',d)

    return render(request,'home.html')

def user_login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        AUO=authenticate(username=username,password=password)
        if AUO:
            if AUO.is_active:
                login(request,AUO)
                request.session['username']=username
                return HttpResponseRedirect(reverse('home'))
            else:
                return HttpResponse('Not an Active User')
        return HttpResponse('Invalid Credentials')
        

    return render(request,'user_login.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))\
    
@login_required
def Profile_display(request):
    username=request.session.get('username')
    UO=User.objects.get(username=username)
    PO=Profile.objects.get(username=UO)
    d={'UO':UO,'PO':PO}
    return render(request,'Profile_display.html',d)

@login_required
def Change_password(request):
    if request.method == 'POST':
        pw=request.POST['pw']
        username=request.session.get('username')
        UO=User.objects.get(username=username)
        UO.set_password(pw)
        UO.save()
        return HttpResponse('Change password successfully')
    return render(request,'Change_password.html')

def Reset_password(request):
    if request.method=='POST':
        user=request.POST['user']
        pw=request.POST['pw']
        username=User.objects.filter(username=user)
    return render(request,'Reset_password.html')