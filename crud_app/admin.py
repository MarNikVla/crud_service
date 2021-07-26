
from django.contrib import admin

from crud_app.models import Profile, CompanyModel

@admin.register(Profile)
class UserModelAdmin(admin.ModelAdmin):
    pass
    # list_display = ['name', 'slug']
    # prepopulated_fields = {'slug': ('name',)}

@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    pass
    # list_display = __all__()
    # list_filter = ['available', 'created', 'updated']
    # list_editable = ['price', 'available']
    # prepopulated_fields = {'slug': ('name',)}