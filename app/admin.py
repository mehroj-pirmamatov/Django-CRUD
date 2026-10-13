from django.contrib import admin

from .models import Category,Book

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=("name",)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=("name",)