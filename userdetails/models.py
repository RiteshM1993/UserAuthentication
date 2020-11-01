from django.db import models
from django.contrib.auth.models import User

class ValidUser(models.Model):

    user_name = models.ForeignKey(User,on_delete=models.CASCADE
    )
    message = models.CharField(
        verbose_name='Messge',
        max_length=100
    )

    class Meta:
        verbose_name = "Valid user"




class InValidUser(models.Model):

    user_name = models.CharField(verbose_name='Username',max_length=50
    )
    message = models.CharField(
        verbose_name='Messge',
        max_length=100
    )

    class Meta:
        verbose_name = "InValid user"