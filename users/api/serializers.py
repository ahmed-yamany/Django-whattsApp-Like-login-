from rest_framework import serializers
from users.models import FamTamUser
from codes.models import Code


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamTamUser
        fields = ['phone_number']

    def save(self, **kwargs):
        user = FamTamUser(
            phone_number=self.validated_data['phone_number']
        )

        user.save()
        return user


class CodeSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(default=None, source='FamTam.phone_number')
    code = serializers.CharField(default=None, source='Code.code')

    class Meta:
        model = Code
        fields = ['phone_number', 'code']
