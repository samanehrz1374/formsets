from django.contrib import admin

# Register your models here.
from .models import Book,Author,ProfileModel,skillsModel


# admin.site.register(Book)
# admin.site.register(Author)




class BookInLineAdmin(admin.TabularInline):
    model = Author


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInLineAdmin]


admin.site.register(Book, AuthorAdmin)



# admin.site.register(Programmer)
# admin.site.register(Language)


class languageInLineAdmin(admin.TabularInline):
    model = skillsModel


class programerrAdmin(admin.ModelAdmin):
    inlines = [languageInLineAdmin]


admin.site.register(ProfileModel, programerrAdmin)