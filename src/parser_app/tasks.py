from celery import shared_task
from .models import ParsingTask
from .services.selenium_service import parse_url


@shared_task
def start_parsing_task(task_id):
    task = ParsingTask.objects.get(id=task_id)
    task.status = 'in_progress'
    task.save()

    try:
        result = parse_url(task.url)
        task.result = result
        task.status = 'success'
    except Exception as e:
        task.result = {'error': str(e)}
        task.status = 'failed'

    task.save()

    return "✅ Парсинг успешно завершён"