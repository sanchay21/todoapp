# Generated by Django 5.1.6 on 2025-02-19 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.ImageField(upload_to='')),
                ('task', models.CharField(max_length=100)),
                ('status', models.IntegerField()),
            ],
        ),
    ]
