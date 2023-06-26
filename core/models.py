from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.CharField('NAME *', max_length=50)
    surname=models.CharField('SURNAME *', max_length=50)
    patronymic=models.CharField('PATRONYMIC *', max_length=250)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name


