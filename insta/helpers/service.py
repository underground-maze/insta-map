import hashlib
import os
import uuid

from django.utils import timezone


def video_path(instance, filename, directory='video'):
    """
    Path to video
    *directory*/ab/cd/abcdef0123456789abcdef0123456789.mov
    """
    basename, ext = os.path.splitext(filename.lower())
    hashed_name = hashlib.md5('{}{}{}'.format(uuid.uuid4(), filename, timezone.now()).encode('utf-8')).hexdigest()
    return os.path.join(directory, hashed_name[:2], hashed_name[2:4], hashed_name + ext)
