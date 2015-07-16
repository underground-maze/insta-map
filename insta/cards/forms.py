from copy import deepcopy

from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator

from captcha.fields import ReCaptchaField

from cards.models import Card
from accounts.models import InstaUser


class AddCardForm(forms.ModelForm):

    """ Create new card instance """

    required_msg = 'Обязательное поле.'
    email_invalid = 'Введите корректный адрес электронной почты.'

    captcha = ReCaptchaField()

    class Meta:
        model = Card
        fields = ('position', 'video', 'description', 'radius', )

    email = forms.EmailField(required=False, max_length=200, error_messages=dict(invalid=email_invalid))

    def __init__(self, *args, **kwargs):
        kwargs = self.prepare_post_data(kwargs)
        super().__init__(*args, **kwargs)
        self.fields['radius'].required = False
        self.fields['video'].required = True
        self.fields['description'].validators = [MaxLengthValidator(1000)]

    def _blank_spaces_less(self, value):
        """ Not allow blank spaces """
        value = value.strip()
        if not value:
            raise ValidationError(self.required_msg)

    def clean_description(self):
        description = self.cleaned_data.get('description', '')
        self._blank_spaces_less(description)
        return description

    def clean_radius(self):
        return 3

    def prepare_post_data(self, kwargs):
        """ Get latitude and longitude from request data """
        self.user = kwargs.pop('user', None)
        position = kwargs['data'].get('position', '')
        if position.strip():
            kwargs['data'] = deepcopy(kwargs['data'])
            kwargs['data'].pop('position')
            try:
                lat, lon = position.strip('()').split(', ')
            except ValueError:
                lat = lon = '0'
            kwargs['data'].update(dict(position_0=lat, position_1=lon))
        return kwargs

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if email and self.user is None:
            self.user, created = InstaUser.objects.get_or_create(email=email)
        return email

    def save(self, *args, **kwargs):
        """ Add user into created instace """
        instance = super().save(commit=False)
        instance.user = self.user
        instance.youtube_id = 'pre-moderated'
        instance.save()
        return instance
