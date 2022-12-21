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

    def __str__(self):
        return f"{self.name}"


class Status(models.Model):
    STATUSES =(
        ('upcoming', 'Upcoming'),
        ('current', 'Current'),
        ('done', 'Done')
    )

    name = models.CharField(choices=STATUSES, default='done', unique=True, max_length=50)

    class Meta:
        verbose_name_plural = 'Statuses'

    def __str__(self):
        return f"{self.name}"


class Role(models.Model):
    ROLES =(
        ('admin', 'Admin'),
        ('hr', 'HR'),
        ('manager', 'Manager'),
        ('employee', 'Employee')
    )

    name = models.CharField(choices=ROLES, default='admin', unique=True, max_length=50)

    def __str__(self):
        return f"{self.name}"


class Template(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Task(models.Model):
    name = models.CharField(max_length=100)
    done = models.BooleanField(default=False)
    template = models.ForeignKey(Template, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    name        = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='employee')
    manager     = models.ForeignKey(Login, on_delete=models.CASCADE, related_name='manager', null=True, blank=True)
    role        = models.ForeignKey(Role, on_delete=models.CASCADE)
    title       = models.CharField(max_length=100, null=True, blank=True)
    department  = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    sign_date   = models.DateField(null=True, blank=True)
    start_date  = models.DateField(null=True, blank=True)
    template    = models.ForeignKey(Template, on_delete=models.SET_NULL, null=True, blank=True, related_name='checklist_template')
    is_new      = models.BooleanField(default=False)
    status      = models.ForeignKey(Status, on_delete=models.CASCADE, related_name='orientation_status')

    def __str__(self):
        return f"{self.name}"

