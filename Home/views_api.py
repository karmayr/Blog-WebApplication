from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from .models import Profile
from .utilities import *


class LoginView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(
                username=data.get('username')).first()

            if check_user is None:
                response['message'] = 'invalid username , user not found'
                raise Exception('invalid username not found')

            # print('@@@@')
            # print('@@@@')
            # print('@@@@')
            # obj = Profile.objects.filter(user = check_user ).first().verified
            # print(obj)
            # print('@@@@')
            # print('@@@@')
            # print('@@@@')
            if not Profile.objects.filter(user = check_user ).first().verified:
                response['message'] = 'Profile Not Verified'
                raise Exception('profile not verified')

            user_obj = authenticate(username=data.get('username'),
                                    password=data.get('password'))
            if user_obj:
                login(request,user_obj)
                response['status'] = 200
                response['message'] = 'Welcome'
            else:
                response['message'] = 'invalid password'
                raise Exception('invalid password')


        except Exception as e:
            print(e)

        return Response(response)


LoginView = LoginView.as_view()
            

class RegisterapiView(APIView):

    def post(self, request):
        response = {}
        response['status'] = 500
        response['message'] = 'Something went wrong'
        try:
            data = request.data

            if data.get('username') is None:
                response['message'] = 'key username not found'
                raise Exception('key username not found')

            if data.get('password') is None:
                response['message'] = 'key password not found'
                raise Exception('key password not found')

            check_user = User.objects.filter(username=data.get('username')).first()

            if check_user:
                response['message'] = 'Username already Taken'
                raise Exception('Username already Taken')

            
            register_obj = User.objects.create(username=data.get('username'))
            register_obj.set_password(data.get('password'))
            register_obj.save()
            
            otp = generate_string(6)
            Profile.objects.create(user = register_obj,token = otp )

            send_otp(otp,data.get('username'))
            response['message'] = 'User Created successfully'
            response['status'] = 200


        except Exception as e:
            print(e)

        return Response(response)

RegisterapiView = RegisterapiView.as_view()