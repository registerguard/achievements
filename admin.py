from django.contrib import admin
from achievements.models import Achievement, Town, Image
from sorl.thumbnail.admin import AdminImageMixin

class TownAdmin(admin.ModelAdmin):
    pass

admin.site.register(Town, TownAdmin)

class ImageInline(AdminImageMixin, admin.TabularInline):
   model = Image
   extra = 0

class AchievementAdmin(admin.ModelAdmin):
    list_display = ('first_name_middle', 'last_name', 'date', 'short_description',)
    list_display_links = ('first_name_middle', 'last_name',)
    list_editable = ('short_description',)
    inlines = [
        ImageInline,
    ]

admin.site.register(Achievement, AchievementAdmin)
