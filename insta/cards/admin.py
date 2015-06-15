from django.contrib import admin

from cards.models import Card, YoutubeLogger


class CardAdmin(admin.ModelAdmin):

    """ Card admin class """

    readonly_fields = ('created_at', 'checked_at', )

    list_display = ('pk', '__str__', 'status', 'pretty_status', 'video_url')
    list_display_links = ('pk', '__str__')
    list_filter = ('status', )

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

    list_display = ('pk', '__str__', 'pretty_status', 'card_link')
    list_display_links = ('pk', '__str__')
    list_filter = ('status', )


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

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(Card, CardAdmin)
admin.site.register(YoutubeLogger, YoutubeLoggerAdmin)
