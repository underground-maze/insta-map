from django.core.context_processors import csrf
from django.views.generic import FormView

from helpers.decorators import render_to_json
from cards.forms import AddCardForm


class AddCardView(FormView):

    """ Add new card api view """

    http_method_names = ('get', 'post', )
    form_class = AddCardForm

    @render_to_json
    def dispatch(self, request, *args, **kwargs):
        if not request.is_ajax() or not request.user.is_authenticated():
            return dict(message='Forbidden'), 403
        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        """ Handles GET requests, and return csrf token for form protect """
        return dict(csrf_token=str(csrf(request)['csrf_token'])), 200

    def form_invalid(self, form):
        return dict(result='errors', errors=form.errors), 400

    def form_valid(self, form):
        self.object = form.save()
        return dict(result='success'), 200

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update(user=request.user)
        return kwargs
