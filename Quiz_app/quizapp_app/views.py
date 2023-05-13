from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import authenticate,login,logout
import random
from django.core.mail import send_mail
from .models import *
from .models import result
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def signup(request):
      if request.method == 'POST':
        username=request.POST.get('username')
        useremail=request.POST.get('email')
        password=request.POST.get('password')
        cpassword=request.POST.get('cpassword')

        if password == cpassword:
            user=User.objects.create_user(username=username,email=useremail,password=password)
            user.save()
            return redirect('/')  
        else:
            messages.error(request,'password not match!!')
      return render(request,'signup.html')

def signin(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            auth.login(request,user)
            if user.is_superuser:
                return redirect('/admin_panel/')
            else:
                return redirect ('/deshboard/')
        else:
            messages.error(request,'user is none')
    return render(request,'signin.html')

def forgot_username(request):
    if request.method=='POST':
        username=request.POST.get('username')
        username1=User.objects.get(username=username)
        if username1 is not None:
            otp=random.randint(1000,9999)
            request.session['otp']= otp
            request.session['username']= username

            subject = 'OTP for reset password'
            message = 'This otp use for forgot password %d' % otp
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [username1.email,]
            send_mail( subject, message, email_from, recipient_list )
            return redirect('/forgot_otp/')
        else:
            messages.error(request,'username is none')
    return render(request,'forgot_username.html')

def forgot_otp(request):
    if request.method=='POST':
        otp= int(request.POST.get('otp'))
        session_otp=request.session.get('otp',None)
        if otp==session_otp:
            return redirect('/forgot_password/')
        else:
            return redirect('/forgot_otp/')
    return render(request,'forgot_otp.html')

def forgot_password(request):
    if request.method=='POST':
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        if password==cpassword:
            username=User.objects.get(username=request.session.get('username'))
            if username is not None:
                username.set_password(password)
                username.save()
                return redirect('/')
            else:
                messages.error(request,'username is none')
                return redirect('forgot_password')
        else:
            messages.error(request,'password does not match !!')
    return render(request,'forgot_password.html')

@login_required
def deshboard(request):
    username=request.user.username
    return render(request,'deshboard.html',{'usrname':username})

@login_required
def question(request):
    user=request.user.username
    if request.method=='POST':
        selectlang=request.POST.get('lang')
        questions=quizapp.objects.filter(language=selectlang)
        quizapp.objects.filter(language=selectlang).update(username=user)
        return render(request,'question.html',{'questions':questions,'language':selectlang,'user':user})
    return render(request,'question.html')

@login_required
def postdata(request):
    user=request.user.username
    if request.method=='POST':  
        lang=request.POST.get('option2')
        que=request.POST.get('question')
        selected_option=request.POST.get('option')
        save_data=result.objects.create(question=que,user_answer=selected_option,language=lang)
        save_data.save()
        result.objects.filter(language=lang).update(username=user)

        admin_ans=quizapp.objects.filter(username=user,language=lang)
        print(admin_ans)
        score=0
        wrong=0
        correct=0
        total=0
        for q in admin_ans:
            total+=1
            if q.ans in request.POST.getlist('option'):
                score+=10
                correct+=1
            else:
                wrong+=1         
        percent = score/(total*10) *100
        context = {
            'score':score,
            'correct':correct,
            'wrong':wrong,
            'percent':percent,
            'total':total
            }
    return render(request,'result.html',context)
  
@login_required
def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def result1(request):
    return render(request,'result.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
