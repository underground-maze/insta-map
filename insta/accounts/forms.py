from django.core.exceptions import ValidationError
from django.core.validators import MinLengthValidator
from django.contrib.auth.forms import PasswordResetForm

from captcha.fields import ReCaptchaField
from registration.forms import RegistrationForm

from accounts.models import InstaUser


class InstaRegistrationForm(RegistrationForm):

    """ Custom registration form """

    class Meta:
        model = InstaUser
        fields = ('email', 'password1', 'password2', 'first_name', 'last_name')

    captcha = ReCaptchaField(label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.required = True
            field.widget.attrs['required'] = 'required'
        # minimum password length
        self.fields['password1'].validators += [MinLengthValidator(6)]
        # remove username fields
        del self.fields['username']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if InstaUser.objects.filter(email__iexact=email):
            raise ValidationError('Пользователь, с таким адресом электронной почты, уже зарегистрирован.')
        return email


class InstaPasswordResetForm(PasswordResetForm):

    """ Custom password reset form """

    captcha = ReCaptchaField(label='')
