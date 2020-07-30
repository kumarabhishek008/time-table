from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.exceptions import *
from django.contrib.auth.decorators import login_required
from .models import timetablecolumn


# Create your views here.
@login_required(login_url='/login')
def index(request):
    user_table1 = timetablecolumn.objects.filter(user= request.user,row = "first")
    user_table2 = timetablecolumn.objects.filter(user=request.user,row= "second")
    user_table3 = timetablecolumn.objects.filter(user=request.user,row= "third")
    user_table4 = timetablecolumn.objects.filter(user=request.user,row= "fourth")
    user_table5 = timetablecolumn.objects.filter(user=request.user,row= "fifth")
    user_table6 = timetablecolumn.objects.filter(user=request.user,row= "sixth")
    
    return render(request,'usertt/index.html',{'usertable_1':user_table1,'usertable_2':user_table2,
                    'usertable_3':user_table3,'usertable_4':user_table4,'usertable_5':user_table5,
                    'usertable_6':user_table6})

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

def DeleteRow(request):
    if request.method=='POST':
        deleteday = request.POST['row']
        deletetable = timetablecolumn.objects.filter(user=request.user,c1=deleteday)
        deletetable.delete()
        return redirect('/')


def AddTable(request):
    add_table = timetablecolumn.objects.create(row="first")
    add_table.save()
    add_table.user.add(request.user)
    add_table.user.set([request.user])
    return redirect('/')

def UpdateRow(request):
    return redirect('/')



'''def editcontent(request):
    form = timetable_form()
    

    if request.method == 'POST':
        ROw = request.POST['row']
        table = timetablecolumn.objects.get(row=ROw)

        form = timetable_form(request.POST,instance=table)
        if form.is_valid:
            form.save()
            return redirect('/')

    return redirect('/')

def delete(request):
    form1 = DeleteRow()
    if request.method=='POST':
        Row = request.POST['row']
        deleterow = timetablecolumn.objects.get(row=Row)
        deleterow.delete()
        form1 = DeleteRow(request.POST,instance=deleterow)
        if form1.is_valid:
            form1.save()
            return redirect('/')
    else:
        return redirect('/')'''