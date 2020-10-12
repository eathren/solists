import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
# Create your models here.
class Lead(models.Model):
    user_author = models.ForeignKey(
        get_user_model(),
        on_delete = models.CASCADE,
        related_name = "author"
    )
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    title=models.CharField(max_length=200)
    author = models.CharField(max_length = 200)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("lead_detail", args=[str(self.id)])
    