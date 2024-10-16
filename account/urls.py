from django.urls import path
from .views import userLogin, userRegistration, userOtpVerify, userLogOut
urlpatterns = [
    path('login', userLogin, name="login"),
    path('register', userRegistration, name="register"),
    path('otp', userOtpVerify, name="otp"),
    path('logout', userLogOut, name="logout")
]