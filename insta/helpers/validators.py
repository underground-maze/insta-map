import os

from django.core.exceptions import ValidationError
from django.conf import settings


def validate_video(video):
    """ Validator for check is video correct """
    # check is correct format use extentions
    ext = os.path.splitext(video.name)[1].lower()
    if ext not in settings.VIDEO_EXT:
        raise ValidationError('Неверный формат видео.')
    # check maximum file size
    if not (settings.VIDEO_MIN_SIZE < video.size < settings.VIDEO_MAX_SIZE):
        raise ValidationError('Недопустимый размер файла.')
    # Maybe need to add a check in the `mime type` or video `duration`,
    # but it is difficult (given that it can be checked only after uploading)
    # and even on YouTube, you can upload `IMAGE.MOV` so that they do not check
    # the `mime type` before uploading.
    # Let it be...
