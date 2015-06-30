from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, TemplateView


class IndexView(TemplateView):

    """ index template view """

    http_method_names = ('get', )
    template_name = 'index.html'


class SiteUpdate(View):

    """ Update site view """

    http_method_names = ('post', )
    template_name = 'index.html'

    @csrf_exempt
    @login_required
    @render_to_json
    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax():
            return dict(result='errors')
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """ Process post for update site """
        form = self.get_form()
        return dict(result='success')


index_view = IndexView.as_view()
