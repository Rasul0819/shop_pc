from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User
class UserCreationFormByMe(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'image',
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
            'phone_num',

        ]


    