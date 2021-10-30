from django.contrib import admin

from .models import ListItem, User

class UserAdmin(admin.ModelAdmin):
	list_display = ('name',)

class ListItemAdmin(admin.ModelAdmin):
	list_display = ('name',)
	


# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(ListItem, ListItemAdmin)
