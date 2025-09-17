from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer) :
    password = serializers.CharField(write_only=True, style={'input_type':'password'} , validators=[validate_password] )
    password2 = serializers.CharField(write_only=True, required=True)
    class Meta :
        model = User
        fields = ('username','first_name','last_name' ,'email','phone_number' ,'address','gender', 'password' , 'password2' , 'is_staff')

    def validate(self,data):
        if data['password'] != data['password2'] :
            raise serializers.ValidationError("passwords don't match")
        return data

    def create(self , validated_data):
        validated_data.pop('password2')
        is_staff = validated_data.pop('is_staff' , False)
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.is_staff = is_staff
        user.save()
        return user

class CustomUserSerializer(serializers.ModelSerializer) :
    class Meta :
        model= User
        fields = '__all__'
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer) :
    def validate(self, attrs):
        data = super().validate(attrs)
        data['user'] = CustomUserSerializer(self.user).data
        return data

