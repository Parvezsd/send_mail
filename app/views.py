from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# from app.models import *
from django.core.mail import send_mail
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
            'Congratulations you applied successfully',
            'syedparvez5577@gmail.com',
            [MUFDO.email],
            fail_silently=False)


            return HttpResponse('REgistration is Successfull')
        else:
            return HttpResponse('Invalid Data')

    return render(request,'register.html',d)