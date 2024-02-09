from django.contrib import admin
from rango.models import Category, Page, PageAdmin
from rango.models import UserProfile


admin.site.register(Page, PageAdmin)
# Register your models here.

admin.site.register(UserProfile)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PostadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
