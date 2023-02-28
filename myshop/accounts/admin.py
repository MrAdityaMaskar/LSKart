from django.contrib import admin

from django.contrib.auth.admin import UserAdmin
from .models import User, UserType
# Register your models here.


from .forms import UserCreationForm, UserChangeForm




# class UserAdmin(UserAdmin):
#     model = User
#     list_display = ('username', 'is_staff', 'is_active')
#     list_filter  = ('username', 'is_staff', 'is_active', 'is_superuser')
    
#     fieldsets = (
#         (None, {'fields':('username','password')}),
#         ('Permissions', {'fields': ('is_staff', ('is_active', 'is_superuser'),)}),
#         ('Important dates', {'fields': ('last_login', 'date_joined')}),
#         ('Advanced options',{
#             'classes':('collapse',),
#             'fields': ('groups','user_permissions'),
            
#         }),
#     )

#     add_fieldsets= (
#         (None,{
#             'classes': ('wide',) ,# class for css
#             'fields': ('username', 'passsword1', 'password2', 'is_staff', 'is_active', 'is_superuser', 'groups')
#         }),
#     )
    
   
class UserAdmin(UserAdmin):
    add_form =UserCreationForm
    form = UserChangeForm
    model= User
    
    list_display = ('username','email','first_name', 'last_name', 'is_staff', 'is_active')

    list_filter = ('username','email','first_name', 'last_name', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields':('username','email','first_name', 'last_name','phone','address', 'password', 'usertype','groups')}),
        ('permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets= (
        (None,{
            'classes': ('wide',) ,# class for css
            'fields': ('username','email', 'password1', 'password2','phone','address', 'is_staff', 'is_active')
        }),
    )
    
    search_fields = ('username','email',)
    ordering = ('username', 'email',)
    
    
admin.site.register(User, UserAdmin)
admin.site.register(UserType)