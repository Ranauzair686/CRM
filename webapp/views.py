from django.shortcuts import render, redirect
from django.contrib.auth.models import User
# from django.http import HttpResponse   #step 14 
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm #step 33 ,65
from django.contrib.auth.models import auth   #step 40
from django.contrib.auth import authenticate  #step 41 
from django.contrib.auth.decorators import login_required    #step 47 
from .models import Record   #step 55

# Create your views here.



#home page 
def home(request):
    # return HttpResponse('Helloworld')  #step 15 create hello world to check your app runs good 
    return render (request , 'webapp/index.html')   # step 23 as in diary



#register
def register(request):
    form=CreateUserForm()

    if request.method == "POST":
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('')
            return redirect("my-login")  #step 44 in diary 

    context = {'form1' : form}
    return render(request, 'webapp/register.html' , context=context )


#login             step 42
def my_login(request):

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return redirect("dashboard")

    context = {'form2':form}

    return render(request, 'webapp/my-login.html', context=context)



#dashboard view

@login_required(login_url='my-login')  #step 48
def dashboard(request):
    my_records = Record.objects.all()    #step 56 
    context = {'records' : my_records}  #step 56 
    return render(request, 'webapp/dashboard.html',context=context)


#create record
@login_required(login_url='my-login')  
def create_record(request):
    #below is step 66
    form=CreateRecordForm
    if request.method == "POST":
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form3':form}
    return render(request, 'webapp/create-record.html' ,context=context)


#update record  step69
@login_required(login_url='my-login')  
def update_record(request ,pk):   #step 71 
    record = Record.objects.get(id=pk)

    form=UpdateRecordForm(instance=record)
    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect("dashboard")
    context = {'form4':form}
    return render(request, 'webapp/update-record.html' ,context=context)


#read or view a single recoird  step 72
@login_required(login_url='my-login')  
def singular_record(request ,pk):
    all_records = Record.objects.get(id=pk)
    context = {'record': all_records}
    return render(request, 'webapp/view-record.html' ,context=context)




#delete a record    step 74 
@login_required(login_url='my-login')  
def delete_record(request ,pk):
    record = Record.objects.get(id=pk)
    record.delete()
    return redirect("dashboard")




#logout function            step 45
def user_logout(request):
    auth.logout(request)
    return redirect("my-login")



