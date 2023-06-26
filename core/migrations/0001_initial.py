# Generated by Django 4.2.2 on 2023-06-22 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='NAME *')),
                ('surname', models.CharField(max_length=50, verbose_name='SURNAME *')),
                ('patronymic', models.CharField(max_length=250, verbose_name='PATRONYMIC *')),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
