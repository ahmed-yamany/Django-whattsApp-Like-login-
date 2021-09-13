from rest_framework import serializers
from users.models import FamTamUser


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = FamTamUser
        fields = ['phone_number']

    def save(self, **kwargs):
        user = FamTamUser(
            phone_number=self.validated_data['phone_number']
        )
        # password = self.validated_data['password']
        # user.set_password(password)
        user.save()
        return user
