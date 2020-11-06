from django.db import models


class Tasks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст задачи')
    created_at = models.DateField(auto_now_add=True, verbose_name='Дата создания')
    date_of_completion = models.DateField(verbose_name='Дата выполнения')
    status = models.BooleanField(default=False, verbose_name='Статус выполнения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['-created_at']