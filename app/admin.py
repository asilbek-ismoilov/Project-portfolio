from django.contrib import admin
from .models import Blog, Category, Portfolio, PortfolioCategory, Contact
from django.utils.html import format_html

admin.site.register((PortfolioCategory, Category, Contact)) 

@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}

    # def image_tag(self, obj):
    #     if obj.image:
    #         return format_html('<img src="{}" style="width: 100px; height: auto;" />', obj.image.url)
    #     return '-'
    # image_tag.short_description = 'Image'


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('image_tag', 'title', 'created_date', 'category')
    prepopulated_fields = {'slug': ('title',)}

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(obj.image.url))
        return '-'
    image_tag.short_description = 'Image'
