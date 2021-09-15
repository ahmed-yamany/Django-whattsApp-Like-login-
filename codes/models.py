from django.db import models
from django.db.models.signals import post_save
from django.dispatch.dispatcher import receiver
from django.conf import settings
from users.models import FamTamUser
import random


class Code(models.Model):
    """
    :Code model:
    :Create random code of six digits for user:
    :when login:
    """
    code = models.CharField(max_length=6, blank=True, verbose_name='code')
    user = models.OneToOneField(FamTamUser, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        """
        :when saved:
        :Create 6 random digits :
        :modify it to code model:
        """
        code_items = [str(random.choice(range(6))) for _ in range(6)]
        self.code = ''.join(code_items)
        super().save(*args, **kwargs)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Code.objects.create(user=instance)
