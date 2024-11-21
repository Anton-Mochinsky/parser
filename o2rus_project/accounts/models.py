from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class User(AbstractUser):
    email = models.EmailField(unique=True)


class SearchHistory(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    part_number = models.CharField(max_length=36)  # Артикул
    search_time = models.DateTimeField(auto_now_add=True)
    results = models.JSONField()  # Сохраняем результаты поиска в формате JSON

    def __str__(self):
        return f"{self.user.username} searched for {self.part_number} at {self.search_time}"