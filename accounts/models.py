import re
import uuid

from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, User, BaseUserManager



class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Usuário', default=uuid.uuid4, max_length=200, unique=True, blank=True, null=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    email = models.EmailField('E-mail', unique=True)
    is_active = models.BooleanField('Ativo', default=True)
    #is_admin = models.BooleanField('Administrador', default=False)
    is_staff = models.BooleanField('Equipe', default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

class Meta:
    verbose_name = 'Usuário'
    verbose_name_plural = 'Usuários'

    def str(self):
        return self.name or self.username

    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(" ")[0]

    def delete(self):
        return super(User, self).delete()