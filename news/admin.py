from django.contrib import admin
from .models import Item
# Register your models here.


@admin.register(Item)
class NewsAdmin(admin.ModelAdmin):
    list_display = ["id", "by", "title", "time", "type", "url"]
