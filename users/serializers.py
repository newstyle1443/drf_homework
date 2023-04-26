from rest_framework import serializers
from . models import User

class SigninSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
    
    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user
    
class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("name","gender","age","introduction","password",)

    def update(self, instance, validated_data):
        instance.password = validated_data.get('password', instance.password)
        instance.name = validated_data.get('name', instance.name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.age = validated_data.get('age', instance.age)
        instance.introduction = validated_data.get('introduction', instance.introduction)
        password = instance.password
        instance.set_password(password)
        instance.save()
        return instance
    
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id","email","name","gender","age","introduction",)