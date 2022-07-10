from django.contrib import admin
from apps.home.models import Contact, Titles, Cover, Category, Inbox, Posts


# Register your models here.

@admin.register(Titles)
class TitleAdmin(admin.ModelAdmin):
    list_display = ['name', 'type', 'created']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['title', 'email', 'phone', 'address', 'created']


@admin.register(Cover)
class CoverAdmin(admin.ModelAdmin):
    list_display = ['title', 'created']


@admin.register(Inbox)
class InboxAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'topic', 'phone', 'created']
    list_filter = ['name']


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ['title']

