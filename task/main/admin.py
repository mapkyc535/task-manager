from django.contrib import admin
from .models import Tasks


class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'status', 'created_at', 'date_of_completion')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_filter = ('status',)


admin.site.register(Tasks, TasksAdmin)

