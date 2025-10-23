from django.contrib import admin
from .models import URL

class URLAdmin(admin.ModelAdmin):
    list_display = ('original_url', 'short_code', 'visits', 'created_at')
    search_fields = ('original_url', 'short_code')

admin.site.register(URL, URLAdmin)
