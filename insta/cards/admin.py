from django.contrib import admin

from cards.models import Card


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


admin.site.register(Card, CardAdmin)
