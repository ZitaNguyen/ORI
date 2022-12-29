from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from resources.models import Resource

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Resource, MyModelAdmin)