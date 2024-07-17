from django.db import models
from django.conf import settings

# Create your models here.
class Category(models.Model):
    class Meta:
        db_table = "category"

    name = models.TextField()
    total_links = models.IntegerField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, default=0, on_delete=models.CASCADE)

class Links(models.Model):
    class Meta:
        db_table = "links"

    name = models.TextField()
    link = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)