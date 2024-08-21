from rest_framework import serializers
# from django.contrib.auth.models import User 
from rest_framework.validators import UniqueValidator
from .models import CustomUser


class userseriaizer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(max_length = 20)

    class Meta:
        model = CustomUser
        fields = ['id','username','email','mobile_number','password','confirm_password']

        extra_kwargs = {
             'email':{
               'validators':[
                   UniqueValidator(
                       queryset=CustomUser.objects.all(),
                       message = ('email already exist')
                    )
                ]
           },
            'password': {
            # 'write_only': True,
            'style': {'input_type': 'password'}
        },
        'confirm_password': {
            # 'write_only': True,
            'style': {'input_type': 'password'}
        }
        }
    
    def validate(self, data):
    # passwor = data.get('password')
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                'password does not match'
            )
        return data
    
    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError(
                'password must be greater than 8 digit'
            )
        return value
    
    def create(self, validated_data):
        user = CustomUser(
            username=validated_data['username'],
            email=validated_data['email'],
            # password=validated_data['password']
        )
        user.set_password(validated_data['password'])
        user.save()
        print('========222===============',user)
        return user

  