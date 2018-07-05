from django.contrib import admin

# Register your models here.
from .models import BaseInfo
class BaseInfoAdmin(admin.ModelAdmin):
    pass


admin.site.register(BaseInfo, BaseInfoAdmin)

