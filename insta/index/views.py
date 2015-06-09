from django.views.generic import TemplateView


class IndexView(TemplateView):

    """ index template view """

    http_method_names = ('get', )
    template_name = 'index.html'


index_view = IndexView.as_view()
