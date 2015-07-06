from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from accounts.models import InstaUser


class InstaUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = InstaUser


class InstaUserAdmin(UserAdmin):

    form = InstaUserChangeForm


admin.site.register(InstaUser, InstaUserAdmin)
