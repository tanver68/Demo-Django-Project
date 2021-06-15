from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ('page_name', 'page_cat', 'user')






