from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


class FamTamUserManager(BaseUserManager):
    def create_user(self, phone_number):
        if not phone_number:
            raise ValueError("User must have a phone number")

        user = self.model(phone_number=phone_number)

        user.save(using=self._db)

        return user

    def create_superuser(self, phone_number, password):
        user = self.create_user(
            phone_number=phone_number,
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


def profile_image_filepath(self, filename):
    return 'profile_images/' + str(self.pk) + '/profile_image.png'


class FamTamUser(AbstractBaseUser):
    """
        user module that creates users via just phone number
    """

    phone_regex = RegexValidator(regex=r'(01)[0-9]{9}',
                                 message="Phone number must be in the format: '201551608020'."
                                         "allowed.")

    username = None
    phone_number = models.CharField(validators=[phone_regex], max_length=12, unique=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='date_joined')
    last_login = models.DateTimeField(auto_now=True, verbose_name='last_login')
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    hide_phone = models.BooleanField(default=True)

    profile_image = models.ImageField(upload_to=profile_image_filepath, null=True, blank=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = FamTamUserManager()

    def __str__(self):
        return self.phone_number

    def get_profile_image_filename(self):
        return str(self.profile_image)[str(self.profile_image).index('profile_images/' + str(self.pk) + "/"):]

    def has_perm(self, *args, **kwargs):
        return self.is_admin

    def has_module_perms(self, *args, **kwargs):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
