from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'overview',
        'text',
        'pub_date',
        'image',
    )


admin.site.register(Post, PostAdmin)
