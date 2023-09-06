from django.contrib import admin
from .models import Book, BookInstance, Author, Language, Genre


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth', 'date_of_death')
    list_filter = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    actions_on_bottom = True
    # fields = (('first_name', 'last_name'), 'date_of_birth', 'date_of_death')
    readonly_fields = ('date_of_death',)
    list_display_links = ('first_name', 'last_name')
    date_hierarchy = 'date_of_birth'

    fieldsets = (
        ('Basic Information', {
            'fields': ('first_name', 'last_name')
        }),
        ('Other Information', {
            'fields': ('date_of_birth', 'date_of_death')
        })
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'language')
    list_filter = ('author', 'language')
    search_fields = ('language__icontains', 'author')
    list_display_links = ('title', 'author')

    filter_horizontal = ('genre',)
    save_on_top = True


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'due_back', 'status')
    list_filter = ('status', 'book')
    search_fields = ('status',)
    readonly_fields = ('book',)


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('title',)
    readonly_fields = ('title',)


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)
