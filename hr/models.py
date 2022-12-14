from django.db import models

from authentication.models import Login


class Department(models.Model):
    DEPARTMENTS = (
        ('admin', 'Administration'),
        ('hr', 'Human resources'),
        ('finance', 'Finance'),
        ('IT', 'IT'),
        ('sales', 'Sales'),
    )

    name = models.CharField(choices=DEPARTMENTS, default='IT', unique=True, max_length=50)


class Status(models.Model):
    STATUSES =(
        ('upcoming', 'Upcoming'),
        ('current', 'Current'),
        ('done', 'Done')
    )

    name = models.CharField(choices=STATUSES, default='upcoming', unique=True, max_length=50)


class Template(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)


class Employee(models.Model):
    name        = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='employee')
    manager     = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='manager', null=True, blank=True)
    role        = models.CharField(max_length=50)
    title       = models.CharField(max_length=100, null=True, blank=True)
    departement = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    sign_date   = models.DateField(null=True, blank=True)
    start_date  = models.DateField(null=True, blank=True)
    template    = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True, related_name='checklist_template')
    is_new      = models.BooleanField(default=True)
    status      = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, null=True, blank=True, default=None, related_name='orientation_status')



