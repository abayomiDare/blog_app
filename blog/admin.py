from django.contrib import admin

from .models import Article, Comment
# Register your models here.

#admin.site.register(Article)
admin.site.register(Comment)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created')
    search_fields = ('title', 'body',)
    prepopulated_fields = dict([('slug',['title'])])
    list_filter = ['status', 'created']    
    list_editable = ['status']    


# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     list_display = ('name', 'article', 'created', 'active')
#     list_filter = ('active', 'created', 'updated')
#     search_fields = ('name', 'email', 'body')