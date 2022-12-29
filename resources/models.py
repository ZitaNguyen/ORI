from django.db import models
from embed_video.fields import EmbedVideoField

from hr.models import Department

class Resource(models.Model):
    CATEGORIES = (
        ('training', 'Training'),
        ('company', 'Company'),
        ('handbook', 'Handbook')
    )

    name         = models.CharField(max_length=100)
    category     = models.CharField(choices=CATEGORIES, default='training', max_length=50)
    sub_category = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    content      = models.TextField(null=True, blank=True)
    video        = EmbedVideoField(null=True, blank=True)

    def __str__(self):
        return f"{self.category, self.name}"