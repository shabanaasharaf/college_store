from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
# def register(request):
#     if request.method=='POST':
#         username=request.POST['username']
#         password = request.POST['password']
#         cpassword = request.POST['cpassword']
#         user=User.objects.create_user(username=username,password=password)
#         user.save();
#     return render(request,"register.html")
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username already exist")
                print("username already exist")
                return redirect('register')
            else:
                 user = User.objects.create_user(username=username,password=password)
                 user.save()
                 print("user created successfully")
                 messages.info(request,"user created successfully")
                 return redirect('login')
        else:
             messages.info(request,"password mismatching")
             print("password mismatching")
             return redirect('register')

        # user = User.objects.create_user(username=username, password=password)
        # user.save();
    return render(request,"register.html")
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,"new_page.html")
        else:
            messages.info(request,"invalid user")
            return redirect('login')
    return render(request,"login.html")
def view(request):
    # if request.method == 'POST':
    # #     username = request.POST.get['username']
    # #     password = request.POST['password']
    # #     user = auth.authenticate(username=username,password=password)
    # #     if user is not None:
    # #         if user.is_active:
    #     return render(request,"personal_info.html")
    return render(request,"personal_info.html")


def info(request):
    if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     cpassword = request.POST['cpassword']
    #     if password == cpassword:
    #         if User.objects.filter(username=username).exists():
        messages.info(request,"user created successfully")
        print("user created successfully")
        # return redirect('/')
        # else:
        #      messages.info(request,"password mismatching")
        #      print("password mismatching")
        #      return redirect('register')
    return render(request,"new_page.html")
def logout(requset):
    auth.logout(request)
    return redirect('/')
def home(request):
    return redirect('/')