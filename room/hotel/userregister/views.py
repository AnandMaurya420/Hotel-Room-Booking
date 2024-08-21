from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CustomUser
from . serializers import userseriaizer

from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import redirect,render
# from rest_framework.authentication import authenticate
from django.contrib.auth import login, authenticate, logout 

from django.core.mail import send_mail
from hotel .settings import EMAIL_HOST_USER
from django.core.mail import EmailMultiAlternatives


from rest_framework.authtoken.serializers import AuthTokenSerializer
import random

import pyotp
from datetime import datetime, timedelta

# Create your views here.

@csrf_exempt
@api_view(['POST'])
def userregister(request):
    DATA = request.data
    print(DATA)
    serializervalidation = userseriaizer(data = request.data)

    if not serializervalidation.is_valid():
        return Response({'status':200, 'error':serializervalidation.errors})
    
    serializervalidation.save()
    # _, token = AuthToken.objects.create(user)

    # subject = 'welcome to GFG world'
    # message = f'Hi {user.username}, thank you for registering in geeksforgeeks.'
    # email_from = settings.EMAIL_HOST_USER
    # recipient_list = [user.email, ]
    # send_mail( subject, message, email_from, recipient_list )

    # return Response({
    #     'user_info':{
    #         'id':user.id,
    #         'username': user.username,
    #         'email': user.email
    #     },
    #     'token':token
    # })
    # return Response({'status':200,'message':'sucessfully register','payload':serializervalidation.data})

@csrf_exempt
@api_view(['PUT'])
def userupdate(request,pk):

    userpassword = request.data
    modelobject = CustomUser.objects.get(id=pk)
    modelobject.set_password(userpassword['password'])
    modelobject.save()
    print('request',request.data)
    
    
    # serializer = userseriaizer(modelobject, data = request.data, partial = True)
    # # print('------------>',serializer.data.get('password'))

    # if not serializer.is_valid():
    #     return Response({'status':200, 'error':serializer.errors})
    # # user = request.data
    # # user.set_password(user['password'])
    
    # serializer.save()
    # print('------------>',serializer.data['password'])
    # # serializer.set_password(serializer.data['password'])
    # # serializer.save()
    # return Response({'status':200,'message':'sucessfully update','payload':serializer.data})


@api_view(['POST'])
@csrf_exempt
def userlogin(request):

    email = request.POST['email']
    password = request.POST['password']

    user = authenticate(email = email, password = password)
    print('user',user)
    if user is not None :
        login(request,user)
        return JsonResponse({'login':'login sucessfully'})
    else:
        return JsonResponse({'login error':'invalid credential'})

@csrf_exempt 
@api_view(['POST'])
def userlogout(request):
    # print(request.session)
    logout(request)
    return JsonResponse({'logout':'logout sucessfully'})

@api_view(['POST'])
def forgot_password(request):
    email = request.POST['email']

    user = User.objects.get(email = email)
    try:
        if user:
            otp = random.randint(1111, 9999)
            print(otp)

            subject = 'OTP for password change'
            from_email = EMAIL_HOST_USER
            to_email = user.email

            text_content = 'This is an important message.'
            html_content = f'<h3>otp</h3> <br>{otp}' 
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            def user_otp(request):
                enter_otp = request.POST['enter_otp']
                if otp == enter_otp:
                    def userpassword(request):
                        password = request.POST['password']
                        confirm_password = request.POST['confirm_password']

                        if password == confirm_password:
                            user.set_password('password')
                            user.save()
                        else:
                           userpassword()
                    return JsonResponse({'message':'password update sucessfully'})      
                else:
                    user_otp()
                    return JsonResponse({'otp_error':'please enter valid otp'})     
        else:
            return JsonResponse({'emial':'email not found'})

    except:
        return JsonResponse({'validation_error':'enter valid email'})


#     print(django.middleware.csrf.get_token(request))

# def generate_otp(request):

#     # totp = pyotp.TOTP(pyotp.random_base32(), interval=300)  # 5 minutes validity
#     totp = random.randint(1111, 9999)
#     return totp

def verify_otp(otp, user_otp):
    return otp == user_otp

def forgot_pass(request):

    if request.method == 'POST':
        email = request.POST['email']
        user = CustomUser.objects.get(email = email)

        if user:

            email_otp = random.randint(1111, 9999)
            print('email otp----------->',email_otp)
            user.email_otp = email_otp
            user.save()

            subject = 'OTP for password change'
            from_email = EMAIL_HOST_USER
            to_email = user.email

            text_content = 'This is an important message.'
            html_content = f'<h3>otp</h3> <br>{email_otp}' 
            msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()

            return redirect('verfying_otp', user_id=user.id)
        else:
            return render(request, 'register.html',{'error':'user email not found'})

    return render(request, 'email.html')

def verfying_otp(request,pk):

    user = CustomUser.objects.get(id=pk)

    if request.method == 'POST':
        em_otp = request.POST['email_otp']

        if verify_otp(em_otp,user.email_otp):
            user.is_email_verified = True
            user.email_otp = None
            user.save()
            return render(request, 'password.html')
        else:
            return render(request, 'userregister/email_verify.html', {'error': 'Invalid OTP'})
        
    return render(request, 'verify_otp.html', {'error': 'Invalid OTP'})

def password_verify(request,pk):

    user = User.objects.get(id=pk)
    if request.method == 'POST':
        
        password = request.POST['password']
        confirm_password = request.POST['confirm_pasword']

        if password == confirm_password:
            user.set_password('password')
            user.save()
        else:
            return render(request, 'userregister/password_change.html', {'error': 'password not match'})
        
    return render(request, 'userregister/password_change.html', {'error': 'Invalid_otp'})
