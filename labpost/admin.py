from django.contrib import admin
from .models import TestModel, TestItem
from .models import User

#customize TestItem list display in django admin
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','name')

class TestModelAdmin(admin.ModelAdmin):
    list_display = ('testName', 'unit', 'minVal', 'maxVal')

class TestItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'testName', 'dateStamp')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(TestModel, TestModelAdmin)
admin.site.register(TestItem, TestItemAdmin)
