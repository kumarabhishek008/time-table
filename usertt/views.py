from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import *
from django.contrib.auth.decorators import login_required
from .models import timetablecolumn
from django.views.decorators.csrf import csrf_exempt
import json


# Create your views here.
@login_required(login_url='/login')
def index(request):
    
    user_table1 = timetablecolumn.objects.filter(user= request.user)[:1]
    
    len_of_usertable = len(user_table1)

    
    return render(request,'usertt/index.html',{'usertable_1':user_table1,'user_len':len_of_usertable})

def register(request):
    if request.method =='POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        try:
            if (password1 == password2):
                if User.objects.filter(username = username).exists():
                    messages.info(request,"email has been taken")
                    return redirect('/register')
                else:
                    user = User.objects.create_user(first_name=first_name,last_name = last_name,username=username,password=password2)
                    user.save()
                    messages.info(request,"you are registered now login here")
                    return redirect('/login')
            else:
                messages.info(request,"passwords are not same")
        except:
            messages.info(request,"please fill the required input")
            return redirect('/register')
    else:
        return render(request,'usertt/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        try:
            if User.objects.filter(username = username).exists():
                try:
                    user = auth.authenticate(request,username = username,password=password)
                except :
                    print("something")
                    messages.info(request," wrong credantials try again or please input valid credantials")
                    return redirect('/login')
                try:
                    if user is not None:
                        auth.login(request,user)
                        return redirect('/')
                    else:
                        messages.info(request,"wrong credantials")
                        return redirect('/login')
                except :
                    messages.info(request,"somthing wrong please contact customer care ")
            else:
                messages.info(request,"you have typed wrong credantials")
                return redirect('/login')
        except :
            messages.info(request,"something wrong")
            return redirect('/login')
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request,'usertt/login.html')

@login_required
def logout(request):
    if request.user.is_authenticated :
        auth.logout(request)
        return redirect('/')




@login_required(login_url='/login')
@csrf_exempt
def UpdateorCreateRow(request):
    if request.method == 'POST':
        update_code = request.POST['code']
        table_id = request.POST['id']
        print("data",table_id)
        if table_id == '' :
            create_table=timetablecolumn.objects.create(c1=update_code)
            create_table.save()
            create_table.user.add(request.user)
            create_table.user.set([request.user]) 
        
        else:  
            if timetablecolumn.objects.filter(user=request.user,id=table_id).exists():
                update_row = timetablecolumn.objects.filter(user=request.user,id=table_id)
                update_row.update(c1=update_code)
                return redirect('/')
    return redirect('/')




      
      