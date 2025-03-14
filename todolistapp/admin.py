from django.contrib import admin
from .models import Taskers , Task

# Register your models here

@admin.register(Taskers)
class TaskerAdmin(admin.ModelAdmin):
    list_display = ('username' , 'email' , 'created_at')
    search_fields = ['username' , 'email'] #enables search function


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title' , 'completed' , 'created_at' , 'taskers')
    search_fields = ('title' , 'completed' , 'taskers__username')
    list_filter = ('completed' , 'taskers__username')
    autocomplete_fields = ('taskers',)