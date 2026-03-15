# Generated manually for Lead model

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(db_index=True, max_length=64, verbose_name='Источник формы')),
                ('payload', models.JSONField(blank=True, default=dict, verbose_name='Данные формы')),
                ('email', models.CharField(blank=True, db_index=True, max_length=254, verbose_name='Email')),
                ('phone', models.CharField(blank=True, db_index=True, max_length=64, verbose_name='Телефон')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Создано')),
            ],
            options={
                'verbose_name': 'Заявка',
                'verbose_name_plural': 'Заявки',
                'ordering': ['-created_at'],
            },
        ),
    ]
