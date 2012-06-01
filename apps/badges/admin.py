from django.contrib import admin

from funfactory.admin import site

from badges.models import BadgePreview, Category, Subcategory
from shared.admin import BaseModelAdmin


class CategoryAdmin(BaseModelAdmin):
    change_list_template = 'smuggler/change_list.html'
site.register(Category, CategoryAdmin)


class SubcategoryAdmin(BaseModelAdmin):
    change_list_template = 'smuggler/change_list.html'
site.register(Subcategory, SubcategoryAdmin)


class BadgePreviewInline(admin.TabularInline):
    """
    Inline editor that lets you add localized preview images directly from a
    badge's admin page.
    """
    model = BadgePreview
    extra = 0
