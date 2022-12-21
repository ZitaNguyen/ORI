from django.contrib import admin
from .models import Employee, Task, Template, Department, Status, Role


admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Template)
admin.site.register(Department)
admin.site.register(Status)
admin.site.register(Role)