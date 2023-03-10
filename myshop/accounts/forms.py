from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import CustomUser
from django import forms


class CreateUserForm(UserCreationForm):
    
    class Meta:
        model = CustomUser
        fields  = ('username','first_name','last_name','phone', 'email', 'usertype', 'groups','password1','address')
        
    
    # class UserChangeForm(UserChangeForm):
        
    #     class Meta:
    #         model: User
    #         fields = ('username', 'email',)
            

        
        
        