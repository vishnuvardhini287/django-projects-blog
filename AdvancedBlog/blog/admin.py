from django.contrib import admin
from .models import Post, Attachment, Comment
class AttachmentInline(admin.TabularInline):
    model = Attachment
    extra = 1

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ('created_at',)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    list_filter = ('created_at', 'tags')
    inlines = [AttachmentInline, CommentInline]
    autocomplete_fields = ['tags']

@admin.register(Attachment)
class AttachmentAdmin(admin.ModelAdmin):
    list_display = ('post', 'file')
    search_fields = ('post__title',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'name', 'created_at')
    search_fields = ('name', 'message')
    list_filter = ('created_at',)
    readonly_fields = ('created_at',)
