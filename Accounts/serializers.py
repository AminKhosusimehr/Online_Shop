from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()
class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , required=True , validators=[validate_password])
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('username' , 'first_name' , 'last_name' ,
                  'email' , 'phone_number' , 'address' ,
                  'gender' , 'password' , 'password2')
    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError('Passwords must match')
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError('Email already registered')
        if User.objects.filter(phone_number=data['phone_number']).exists():
            raise serializers.ValidationError('Phone number already registered')

        return data

    def create(self , validated_data):
        validated_data.pop('password2' , None)
        user = User.objects.create_user(**validated_data)
        user.set_password(validated_data['password'])
        return user


