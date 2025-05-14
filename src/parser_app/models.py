from django.db import models


class ParsingTask(models.Model):
    url = models.URLField()
    status = models.CharField(max_length=20, default='pending')
    result = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Task for {self.url}"