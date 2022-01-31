from django.contrib import admin
from blog.models import Article, Comment

# Register your models here.
admin.site.register(Article)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'article', 'created', 'active',)
    list_filter = ('active', 'created', 'updated',)
    # list_editable = ('active',)