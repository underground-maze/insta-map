from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm

from accounts.models import InstaUser


class InstaUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm.Meta):
        model = InstaUser


class InstaUserAdmin(UserAdmin):

    form = InstaUserChangeForm

    list_display = UserAdmin.list_display + ('has_cards', )

    def has_cards(self, obj):
        return obj.card_set.all().exists()
    has_cards.boolean = True
    has_cards.short_description = 'Карточки'


admin.site.register(InstaUser, InstaUserAdmin)
