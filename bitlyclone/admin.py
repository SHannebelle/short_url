from django.contrib import admin
from .models import ShortUrl

class ShortUrlAdmin(admin.ModelAdmin):
    list_display = ('url','code','date','username','nb_access')
    list_filter = ('username',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_field = ('url',)

admin.site.register(ShortUrl, ShortUrlAdmin)
