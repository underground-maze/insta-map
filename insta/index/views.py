import json

from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView

from cards.models import Card

from helpers.coordinates import get_map_polygons, get_map_markers
from helpers.service import render_to_file, write_js
from helpers.decorators import render_to_json


class IndexView(TemplateView):

    """ index template view """

    http_method_names = ('get', )
    template_name = 'index.html'


class SiteUpdate(View):

    """ Update site view """

    http_method_names = ('post', )
    template_name = 'index.html'

    @csrf_exempt
    @render_to_json
    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax() or not request.user.is_staff:
            return dict(message='Forbidden'), 403
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Process post for update site """
        # update javascript
        active = Card.active.all()
        # get js representation of card polygons
        polygons = get_map_polygons([card.as_tuple() for card in active])
        markers = get_map_markers([card.as_dict() for card in active])
        markers_data = json.dumps({card.pk: card.as_dict() for card in active})
        # write the script into file
        write_js(polygons, markers, markers_data)
        # update index.html
        render_to_file(self.template_name, {}, self.template_name)
        return dict(result='success'), 200


class IndexMenuView(View):

    """ View for ajax return index page header menu """

    http_method_names = ('get', )

    @render_to_json
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return dict(result='anonymous'), 200

        return dict(result='authenticated', username=request.user.preaty_name), 200
