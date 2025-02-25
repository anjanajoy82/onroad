from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import *
from .forms import *
from django.conf import settings
from django.core.mail import send_mail
import secrets,string


def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')


def user_login(request):
    if request.method == 'POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            print("11111111111111111")
            user=authenticate(request,username=form.cleaned_data['username'],password=form.cleaned_data['password'])
            if user is not None:
                print("22222222222")
                users=Register.objects.get(username=user.username)
                print(users)
                if users.is_approved==True:
                    print("333333333333")
                    login(request,users)
                    request.session['ut']=users.usertype
                    request.session['uid']=users.id
                    request.session['uname']=users.username
                    messages.success(request,"login succesfull",extra_tags="success")
                    return redirect('/')
                else:
                    messages.error(request,"u can continue after admin Approval",extra_tags="error")
            else:
                messages.error(request,"invalid username and password",extra_tags="error")
        else:
            messages.error(request,"login failed",extra_tags="error")
            print(form.errors)
            form=LoginForm()
    else:
        form=LoginForm()
    return render(request,'login.html',{'form':form})
    


def registration_type(request):
    return render (request, 'registration_type.html')

def reg(request):
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        print(form)
        if form.is_valid():
            
            # checking the email exists or not
            email = form.cleaned_data['email']
            print(email)
            data = Register.objects.filter(email=email)
            if data:
                print(data)
                messages.error(request,"A user with this email already exists.",extra_tags='error')
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="user"
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"registration successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"registration failed",extra_tags="error")
            print(form.errors)
            form=RegisterForm()
            return render(request,'reg.html',{'form':form,'title':'REGISTRATION'})
    else:
        form=RegisterForm()
    return render(request,'reg.html',{'form':form,'title':'REGISTER'}) 



def home(request):
    return render(request,'home.html')


def user_logout(request):
    logout(request)
    messages.success(request,"logout sucesssfully",extra_tags="success")
    return redirect('/')

#paste into views.py (!!! already athil ulath onum kalayaruth last kondoit paste chytha mathy)

def about(request):
    return render (request, 'about.html')
def contact(request):
    return render (request, 'contact.html')
def furnitures(request):
    return render (request, 'furnitures.html')
def testimonial(request):
    return render (request, 'testimonial.html')


def view_user(request):
    users=Register.objects.filter(usertype="user")
    return render(request,'users.html',{'users':users})


def profile(request):
    user=request.user
    user=Register.objects.get(id=user.id)
    return render(request,'profile.html',{'user':user})

def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = EditProfileForm(instance=request.user)

    return render(request, 'reg.html', {'form': form,'title':'UPDATE'})

def forgot_password(request):
        if request.method =='POST':
            form=ForgotPasswordForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                data = Register.objects.filter(email=email)
                if data:
                    new_password=generate_random_password()
                    user=Register.objects.get(email=email)
                    Reset.objects.create(otp=new_password,user=user)
                    subject="Reset password"
                    message=f"your one time password is {new_password}"
                    email_from=settings.EMAIL_HOST_USER
                    email_to=[email]
                    send_mail(subject, message, email_from, email_to)
                    messages.success(request,'OTP successfully sent',extra_tags='success')
                    return redirect('reset_password')
                else:
                    messages.error(request,'email does not exist',extra_tags='error')
            else:
                messages.error(request,'invalid form data')
        else:
            form=ForgotPasswordForm()
        return render(request,'forgot_password.html',{'form':form})

def generate_random_password(length=6):
    characters=string.ascii_letters+string.digits
    password=''.join(secrets.choice(characters) for _ in range(length))
    return password
def reset_password(request):
    if request.method == 'POST':
        form=ResetPasswordForm(request.POST)
        if form.is_valid():
            otp=form.cleaned_data['otp']
            email=form.cleaned_data['email']
            user = Register.objects.get(email=email)
            user_otp=Reset.objects.filter(user=user).first()
            if user_otp.otp == otp:
                newpassword=form.cleaned_data['new_password']
                data=Register.objects.get(id=user.id)
                data.password=make_password(newpassword)
                data.save()

                user_otp.delete()

                messages.success(request,"Password changed", extra_tags="success")
                return redirect('user_login')
            else:
                messages.error(request,"Inavalid otp", extra_tags="error")
        else:
            messages.error(request,"Inavalid form data", extra_tags="error")
    else:
        form=ResetPasswordForm()
    return render(request,'reset_password.html',{'form':form})



def delete_user(request,id):
    user=Register.objects.get(id=id)
    subject="Account Deletion Notification"
    message=f"Dear {user.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[user.email]
    send_mail(subject, message, email_from, email_to)

    user.delete()
    messages.success(request,'user deleted successfully',extra_tags='success')
    return redirect('view_user')


def delete_mechanic(request,id):
    mechanic=Register.objects.get(id=id)
    subject="Account Deletion Notification"
    message=f"Dear {mechanic.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[mechanic.email]
    send_mail(subject, message, email_from, email_to)

    mechanic.delete()
    messages.success(request,'mechanic deleted successfully',extra_tags='success')
    return redirect('view_mechanic')


def delete_petrol(request,id):
    petrol=Register.objects.get(id=id)
    subject="Account Deletion Notification"
    message=f"Dear {petrol.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[petrol.email]
    send_mail(subject, message, email_from, email_to)

    petrol.delete()
    messages.success(request,'Petrol Pump deleted successfully',extra_tags='success')
    return redirect('view_petrol')

def delete_agent(request,id):
    agent=Register.objects.get(id=id)
    subject="Account Deletion Notification"
    message=f"Dear {agent.username} Your account is being deleted. You will no longer have access to your account. Please register again for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[agent.email]
    send_mail(subject, message, email_from, email_to)

    agent.delete()
    messages.success(request,'Delivery Agent deleted successfully',extra_tags='success')
    return redirect('view_delivery_agents')


def mechreg(request):
    if request.method == 'POST':
        form=MechanicForm(request.POST)
        print(form)
        if form.is_valid():
            # checking the email exists or not
            email = form.cleaned_data['email']
            print(email)
            data = Register.objects.filter(email=email)
            if data:
                print(data)
                messages.error(request,"A user with this email already exists.",extra_tags='error')
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="mechanic"
                user.is_approved=False
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"registration successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"registration failed",extra_tags="error")
            print(form.errors)
            form=MechanicForm()
            return render(request,'mechreg.html',{'form':form,'title':'REGISTER MECHANIC'})
    else:
        form=MechanicForm()
    return render(request,'mechreg.html',{'form':form,'title':'REGISTER MECHANIC'})


def view_mechanic(request):
    mechanics=Register.objects.filter(usertype="mechanic")
    return render(request,'viewmech.html',{'mechanics':mechanics})

def mechanic_profile(request):
    mechanic=request.user
    mechanic=Register.objects.get(id=mechanic.id)
    return render(request,'mechanic_profile.html',{'mechanic':mechanic})

def edit_mechanic_profile(request):
    if request.method == 'POST':
        form = MechanicEditProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('mechanic_profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = MechanicEditProfileForm(instance=request.user)

    return render(request, 'reg.html', {'form': form,'title':'UPDATE MECHANIC'})

def petrolreg(request):
    if request.method == 'POST':
        form=PetrolForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            # checking the email exists or not
            email = form.cleaned_data['email']
            print(email)
            data = Register.objects.filter(email=email)
            if data:
                print(data)
                messages.error(request,"A user with this email already exists.",extra_tags='error')
                return redirect('user_login')
            else:
                user=form.save(commit=False)
                user.usertype="petrol"
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"registration successfull",extra_tags="success")
                return redirect('user_login')
        else:
            messages.error(request,"registration failed",extra_tags="error")
            print(form.errors)
            form=PetrolForm()
            return render(request,'petrolreg.html',{'form':form,'title':'REGISTER PETROL PUMP'})
    else:
        form=PetrolForm()
    return render(request,'petrolreg.html',{'form':form,'title':'REGISTER PETROL PUMP'})


def view_petrol(request):
    petrols=Register.objects.filter(usertype="petrol")
    return render(request,'view_petrol.html',{'petrols':petrols})

def petrol_profile(request):
    petrol=request.user
    petrol=Register.objects.get(id=petrol.id)
    return render(request,'petrol_profile.html',{'petrol':petrol})

def edit_petrol_profile(request):
    if request.method == 'POST':
        form = PetrolEditProfileForm(request.POST,request.FILES, instance=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Prevent user from being logged out
            messages.success(request, "Profile updated successfully.", extra_tags="success")
            return redirect('petrol_profile')  # Redirect to the profile page
        else:
            messages.error(request, "Profile update failed. Please check your form.", extra_tags="error")
    else:
        form = PetrolEditProfileForm(instance=request.user)

    return render(request, 'reg.html', {'form': form,'title':'UPDATE PETROL PUMB'})


def approve_mech(request,id):
    mech=Register.objects.get(id=id)
    mech.is_approved=True
    mech.save()
    messages.success(request,'Mechanic approved successfully',extra_tags="success")
    return redirect('view_mechanic')

def reject_mech(request,id):
    mechanic=Register.objects.get(id=id)
    subject="Account Rejection Notification"
    message=f"Dear {mechanic.username} Your registration is being Rejected. Please register again with valid details for future use..."
    email_from=settings.EMAIL_HOST_USER
    email_to=[mechanic.email]
    send_mail(subject, message, email_from, email_to)

    mechanic.delete()
    messages.success(request,'mechanic rejected successfully',extra_tags='success')
    return redirect('view_mechanic')

def deliveryagentreg(request):
    if request.method == 'POST':
        form=DeliveryAgentRegForm(request.POST,request.FILES)
        print(form)
        if form.is_valid():
            # checking the email exists or not
            email = form.cleaned_data['email']
            print(email)
            data = Register.objects.filter(email=email)
            if data:
                print(data)
                messages.error(request,"A user with this email already exists.",extra_tags='error')
                return redirect('/')
            else:
                user=form.save(commit=False)
                user.usertype="deliveryagent"
                user.pump_id=request.user.id
                user.is_approved=True
                user.password = make_password(form.cleaned_data['password'])
                user.save()
                messages.success(request,"registration successfull",extra_tags="success")
                return redirect('/')
        else:
            messages.error(request,"registration failed",extra_tags="error")
            print(form.errors)
            form=DeliveryAgentRegForm()
            return render(request,'mechreg.html',{'form':form,'title':'REGISTER DELIVERY AGENT'})
    else:
        form=DeliveryAgentRegForm()
    return render(request,'mechreg.html',{'form':form,'title':'REGISTER DELIVERY AGENT'})

def view_agent(request):
    agents=Register.objects.filter(usertype="deliveryagent")
    return render(request,'view_delivery_agents.html',{'agents':agents})

def agent_profile(request):
    agent=request.user
    agent=Register.objects.get(id=agent.id)
    return render(request,'agent_profile.html',{'agent':agent})

# def view_near_mech(request):
#     mechanics=Register.objects.filter(usertype="mechanic", is_approved=True)
#     return render(request,'view_near_mech.html',{'mechanics':mechanics})
def add_fuel_detail(request):
    if request.method == "POST":
        form = FuelForm(request.POST)
        if form.is_valid():
            fuel_detail = form.save(commit=False)
            fuel_detail.petrol = request.user  # Assign current petrol pump user
            fuel_detail.save()
            return redirect('view_fuel_detail')  # Redirect after adding fuel
    else:
        form = FuelForm()
    return render(request, 'add_fuel_detail.html', {'form': form})


def view_fuel_details(request):
    fuel_details = FuelDetail.objects.filter(petrol=request.user)
    return render(request, 'view_fuel_detail.html', {'fuel_details': fuel_details})
