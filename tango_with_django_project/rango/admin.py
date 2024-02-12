from django.contrib import admin
from rango.models import Category, Page, PageAdmin
<<<<<<< HEAD

admin.site.register(Page, PageAdmin)
# Register your models here.

=======
from rango.models import UserProfile


admin.site.register(Page, PageAdmin)
# Register your models here.

admin.site.register(UserProfile)
>>>>>>> 3aad359ab85a6c495c7cda84e8e25252d0da2bbd

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)

class PostadAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
