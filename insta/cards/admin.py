from django.contrib import admin

from cards.models import Card, YoutubeLogger


class CardStatusFilter(admin.SimpleListFilter):

    """ Filter to select cards 'new', 'accepted', 'rejected' """

    title = 'Статус'
    parameter_name = 'status'

    def lookups(self, request, model_admin):
        return Card.STATUS_CHOICES

    def queryset(self, request, queryset):
        value = self.value()
        if value in (status[0] for status in Card.STATUS_CHOICES):
            return queryset.filter(status=value)
        return queryset


class CardAdmin(admin.ModelAdmin):

    """ Card admin class """

    readonly_fields = ('created_at', 'checked_at', )

    list_display = ('pk', '__str__', 'status', 'pretty_status', 'video_url')
    list_display_links = ('pk', '__str__')
    list_filter = (CardStatusFilter, )

    def pretty_status(self, obj):
        if obj.is_new:
            return None
        return obj.is_accepted
    pretty_status.boolean = True
    pretty_status.short_description = 'Статус'

    def video_url(self, obj):
        if obj.video_url:
            return '<a href="{url}">{id}</a>'.format(url=obj.video_url, id=obj.youtube_id)
    video_url.allow_tags = True
    video_url.short_description = 'Видео на youtube'


class YoutubeLoggerAdmin(admin.ModelAdmin):

    """ YoutubeLogger admin class """

    readonly_fields = ('card', 'upload_at', 'status', 'description', )
    fields = ('card_link', 'upload_at', 'status', 'description', )

    list_display = ('pk', '__str__', 'pretty_status', )
    list_display_links = ('pk', '__str__')

    def pretty_status(self, obj):
        return obj.is_success
    pretty_status.boolean = True
    pretty_status.short_description = 'Статус'

    def card_link(self, obj):
        return '<a href="/admin/cards/card/{card}/">{card_info}</a>'.format(
            card=obj.card.pk, card_info=str(obj.card))
    card_link.allow_tags = True
    card_link.short_description = 'Карточка'

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request):
        return False


admin.site.register(Card, CardAdmin)
admin.site.register(YoutubeLogger, YoutubeLoggerAdmin)
