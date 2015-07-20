import json
import hashlib
import os
import uuid

from django.conf import settings
from django.utils import timezone
from django.template.loader import render_to_string

from helpers.coordinates import get_map_polygons, get_map_markers


def video_path(instance, filename, directory='video'):
    """
    Path to video
    *directory*/abcdef0123456789abcdef0123456789.mov
    """
    basename, ext = os.path.splitext(filename.lower())
    hashed_name = hashlib.md5('{}{}{}'.format(uuid.uuid4(), filename, timezone.now()).encode('utf-8')).hexdigest()
    return os.path.join(directory, hashed_name + ext)


def write_js(polygons, markers, cards_data):
    """ Create js file with map data """
    path = os.path.join(settings.STATIC_ROOT, 'maps')
    if not os.path.exists(path):
        os.makedirs(path)
    path = os.path.join(path, 'polygon_path.js')
    content = 'var polygons=[{polygons}],markers=[{markers}],cards={cards};'.format(
        polygons=polygons, markers=markers, cards=cards_data)
    with open(path, 'w', encoding='UTF-8') as js:
        js.write(content)


def render_to_file(template_name, context=None, file_name=None):
    """ Render html to file put file in BASE_DIR/markup/*file_name* """
    context = context or dict()
    file_name = file_name or template_name
    context.update(dict(STATIC_URL=settings.STATIC_URL))
    file_path = os.path.join(settings.BASE_DIR, 'markup', file_name)
    with open(file_path, 'w', encoding='UTF-8') as output:
        output.write(render_to_string(template_name, context))


def site_update(active, template_name):
    """ Recalculate all coordinates and place new files """
    # get js representation of card polygons
    polygons = get_map_polygons([card.as_tuple() for card in active])
    markers = get_map_markers([card.as_dict() for card in active])
    markers_data = json.dumps({card.pk: card.as_dict() for card in active})
    # write the script into file
    write_js(polygons, markers, markers_data)
    # update index.html
    render_to_file(template_name)
