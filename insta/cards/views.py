from django.core.context_processors import csrf
from django.views.generic import FormView

from cards.models import Card
from helpers.decorators import render_to_json


class AddCardView(FormView):

    """ Add new card api view """

    http_method_names = ('get', 'post', )

    @render_to_json
    def dispatch(self, request, *args, **kwargs):
        # if not request.is_ajax():
        #     return dict(result='errors'), 400
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """ Handles GET requests, and return csrf token for form protect """
        return dict(csrf_token=str(csrf(request)['csrf_token'])), 200

    def form_invalid(self, form):
        return dict(status='errors', errors=form.errors), 400

    def form_valid(self, form):
        super().form_valid(form)
        return dict(status='success'), 200


add_card_view = AddCardView.as_view()
