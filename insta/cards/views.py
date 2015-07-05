from django.views.generic import FormView

from cards.models import Card
from helpers.decorators import render_to_json, ajax


class AddCardView(FormView):

    """ Add new card api view """

    http_method_names = ('post', )

    @render_to_json
    @ajax
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)



add_card_view = AddCardView.as_view()
