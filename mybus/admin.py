from django.contrib import admin

from .models import BusInfo, BusNo


class BusInfoAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'owner', 'is_public', 'date_updated','latitude','longitude')
    list_editable = ('is_public',)
    list_filter = ('is_public', 'owner__username')
    search_fields = ['url', 'title']
    readonly_fields = ('date_created', 'date_updated')


admin.site.register(BusInfo, BusInfoAdmin)
admin.site.register(BusNo)
