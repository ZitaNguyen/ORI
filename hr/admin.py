from django.contrib import admin
from .models import Manager, Employee, Task, Template


admin.site.register(Manager)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Template)