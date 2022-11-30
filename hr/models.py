from django.db import models


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
        ('done', 'Done'),
        ('overdue', 'Overdue')
    )

    name = models.CharField(choices=STATUSES, default='upcoming', unique=True, max_length=50)


class Template(models.Model):
    name = models.CharField(max_length=100)


class Task(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)


class Manager(models.Model):
    name        = models.CharField(max_length=100)
    department  = models.ForeignKey(Department, on_delete=models.CASCADE)


class Employee(models.Model):
    name        = models.CharField(max_length=100)
    title       = models.CharField(max_length=100)
    departement = models.ForeignKey(Department, on_delete=models.CASCADE)
    manager     = models.ForeignKey(Manager, on_delete=models.SET_NULL, null=True)
    sign_date   = models.DateTimeField()
    start_date  = models.DateTimeField()
    template    = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, related_name='checklist_template')
    status      = models.ForeignKey(Status, on_delete=models.SET_DEFAULT, default='upcoming')



