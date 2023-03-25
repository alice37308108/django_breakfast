from django.contrib import admin
from .models import Breakfast, Category, Tag


@admin.register(Breakfast)
class BreakfastAdmin(admin.ModelAdmin):
    list_display = ('date', 'breakfast',)  # 管理サイトでモデルの一覧表示時に表示するフィールドのリストを指定する
    search_fields = ('date', 'breakfast',)  # 管理サイトでモデルの検索を行う際に検索対象のフィールドを指定する


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
