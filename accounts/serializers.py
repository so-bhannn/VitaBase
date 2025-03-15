from .models import CustomUser
from rest_framework import serializers

class UserRegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model= CustomUser
        fields=['email', 'password', 'name', 'age', 'gender', 'is_doctor', 'is_patient']
        extra_kwargs={
            'password':{'write_only':True},
            'unique_id': {'read_only': True}
        }

    def validate(self, attrs):
        is_doctor=attrs.get('is_doctor')
        is_patient=attrs.get('is_patient')

        if is_doctor and is_patient:
            raise serializers.ValidationError("User can have only one role- Doctor or Patient.")
        if not is_doctor and not is_patient:
            raise serializers.ValidationError("User has no roles.")
        return attrs

    def validate_email(self, email):
        if CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError("email already exists")
        return email
    
    def create(self, validated_data):
        try:
            user= CustomUser.objects.create_user(**validated_data)
            return user
        except:
            raise serializers.error