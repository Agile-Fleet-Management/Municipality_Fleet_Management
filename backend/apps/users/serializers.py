from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name', 'role', 'picture']
        extra_kwargs = {'password': {'write_only': True, 'required': False}}

    def create(self, validated_data):
        
        user = User(
            username=validated_data['username'],
            email=validated_data['email'],
            picture=validated_data.get('picture'),
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name'),
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.username = validated_data.get('username', instance.username)
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.role = validated_data.get('role', instance.role)
        instance.picture = validated_data.get('picture', instance.picture)

        password = validated_data.get('password')
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance

class UserInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'role','picture']
