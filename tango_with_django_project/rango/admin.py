from django.contrib import admin
from rango.models import Category, Page, PageAdmin

admin.site.register(Page, PageAdmin)
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PostadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
