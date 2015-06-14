import os

from django.core.exceptions import ValidationError
from django.conf import settings


def validate_video(video):
    """ Validator for check is video correct """

    ext = os.path.splitext(video.name)[1].lower()
    if ext not in settings.VIDEO_EXT:
        raise ValidationError('Неверный формат видео.')

    # raise ValidationError('xxx')
