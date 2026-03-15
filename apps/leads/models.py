from django.db import models


class Lead(models.Model):
    source = models.CharField('Источник формы', max_length=64, db_index=True)
    payload = models.JSONField('Данные формы', default=dict, blank=True)
    email = models.CharField('Email', max_length=254, blank=True, db_index=True)
    phone = models.CharField('Телефон', max_length=64, blank=True, db_index=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.source} — {self.email or self.phone or self.created_at}'
