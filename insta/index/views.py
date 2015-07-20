from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView

from helpers.decorators import render_to_json
from cards.tasks import site_update_task


class IndexView(TemplateView):

    """ index template view """

    http_method_names = ('get', )
    template_name = 'index.html'


class SiteUpdate(View):

    """ Update site view """

    http_method_names = ('post', )

    @csrf_exempt
    @render_to_json
    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax() or not request.user.is_staff:
            return dict(message='Forbidden'), 403
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Process post for update site """
        site_update_task.delay()
        return dict(result='success'), 200


class IndexMenuView(View):

    """ View for ajax return index page header menu """

    http_method_names = ('get', )

    @render_to_json
    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return dict(result='anonymous'), 200

        return dict(result='authenticated', username=request.user.preaty_name), 200
