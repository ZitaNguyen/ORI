# Generated by Django 4.1.3 on 2022-12-27 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0002_alter_status_options_remove_employee_template_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='task',
            field=models.ManyToManyField(blank=True, to='hr.task'),
        ),
    ]
