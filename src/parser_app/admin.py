from django.contrib import admin
from .models import ParsingTask
from .tasks import start_parsing_task


@admin.register(ParsingTask)
class ParsingTaskAdmin(admin.ModelAdmin):
    list_display = ('url', 'status', 'created_at', 'updated_at')
    actions = ['run_parsing_task']

    def run_parsing_task(self, request, queryset):
        for task in queryset:
            start_parsing_task.delay(task.id)
        self.message_user(request, "Парсинг задач добавлен в очередь.")