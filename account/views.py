from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout

# Create your views here.

def userLogin(request):
    return render(request, 'account/login.html')

def userRegistration(request):
    return render(request, 'account/register.html')

def userOtpVerify(request):
    return render(request, 'account/otp.html')

def userLogOut(request):
    # logging out user
    logout(request)
    
    return redirect('homepage')