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
    logo = models.ImageField(upload_to = 'logos/', blank=True)
    id = models.UUIDField(
        primary_key = True,
        default = uuid.uuid4,
        editable = False)
    title=models.CharField(max_length=200)
    author = models.CharField(max_length = 200)

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index')
        ]
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("lead_detail", kwargs={'pk': str(self.pk)})

    