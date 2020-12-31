from django.contrib import admin
from .models import Book, Review
# Register your models here.

class ReviewInline(admin.TabularInline): # specifying a display of TabularInline206.
    model = Review


class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "price",)
    inlines = [ReviewInline,]



admin.site.register(Book, BookAdmin),