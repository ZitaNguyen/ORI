# Generated by Django 4.1.3 on 2022-12-27 21:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_employee_task'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='done',
        ),
    ]
