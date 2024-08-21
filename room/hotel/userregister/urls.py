from django.urls import path
from .views import userupdate, userregister
from userregister import views

urlpatterns = [
    path('register/',views.userregister),
    path('update/<int:pk>/',views.userupdate),
    path('login/',views.userlogin),
    path('logout/',views.userlogout),
    # path('forgotpassword/',views.forgot_password),
    path('forgot_pass/',views.forgot_pass,name='verfying_otp'),
    path('verfying_otp/',views.verfying_otp),
]