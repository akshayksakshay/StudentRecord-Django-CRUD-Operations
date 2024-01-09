from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import studentdetails,MarkList
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def homepage(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            messages.success(request, 'Username and Password does not match')

    return render(request,'homepage.html')

def registration(request):
    if request.POST:
        username = request.POST['username']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1==pass2:
        #print(username,pass1,pass2)
            data = User.objects.create_user(username=username,password = pass1)
            messages.success(request, 'Congratulations!! Registered Successfully')
            data.save()
            return redirect('home')
        else:
            messages.success(request, 'Password Not Match')
    return render(request,'registerpage.html')

def logoutuser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='home')
def addstud(request):
    if request.POST:
        form = StudentForm(request.POST,request.FILES) #request.FILES for uploading images
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            print(form.errors)
    else:
        form = StudentForm()
    return render(request,'add.html',{'fm':form})

@login_required(login_url='home')
def studdash(request):
    data = studentdetails.objects.all()
    return render(request,'dashboard.html',{'data': data})

@login_required
def editdata(request,pk):
    data = studentdetails.objects.get(id = pk)
    if request.POST:
        form = StudentForm(request.POST,request.FILES,instance = data)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = StudentForm(instance = data)
    return render(request,'add.html',{'fm':form})

@login_required
def deletedata(request,pk):
    data = studentdetails.objects.get(id = pk)
    data.delete()
    return redirect('dashboard')

def marklist(request):
    data = MarkList.objects.all()

    return render(request,'marklist.html',{'data':data})

def addmarklist(request,sname):
    if request.POST:
        user = request.user
        studname = studentdetails.objects.get(sname = sname)
        date = request.POST['date']
        sub1 = request.POST['sub1']
        mark1 = request.POST['mark1']
        sub2 = request.POST['sub2']
        mark2 = request.POST['mark2']
        sub3 = request.POST['sub3']
        mark3 = request.POST['mark3']
        sub4 = request.POST['sub4']
        mark4 = request.POST['mark4']
        sub5 = request.POST['sub5']
        mark5 = request.POST['mark5']
        total = int(mark1)+int(mark2)+int(mark3)+int(mark4)+int(mark5)
        data = MarkList(user=user, sname=studname, date=date, sub1=sub1, mark1=mark2, sub2=sub2, mark2=mark2, sub3=sub3, mark3=mark3, sub4=sub4, mark4=mark4, sub5=sub5, mark5=mark5, total=total)
        data.save()
        return redirect('marklist')
    return render(request,'addmarklist.html')

def deletemarklist(request,pk):
    data = MarkList.objects.get(pk = pk)
    data.delete()
    return redirect('marklist')

def filterdept(request,data):
    if data=='CS' or data =='BM' or data =='HM' or data =='CM':
        dt = MarkList.objects.filter(sname__sdept = data) #sdept object is in another table.
    elif data=='clear':
        dt = MarkList.objects.all()
    
    return render(request,'marklist.html',{'data':dt})