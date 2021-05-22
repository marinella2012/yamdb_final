from django.contrib import admin

from ..models.genre import Genre


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    list_filter = ('name', )
    search_fields = ('name', 'slug',)
