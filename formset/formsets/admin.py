from django.contrib import admin

# Register your models here.
from .models import Book,Author


# admin.site.register(Book)
# admin.site.register(Author)




class BookInLineAdmin(admin.TabularInline):
    model = Author


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]


admin.site.register(Book, AuthorAdmin)