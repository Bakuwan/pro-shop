import uuid
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProductEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)  # tambahkan baris ini
    name = models.CharField(max_length=255)
    price = models.IntegerField(default=0)
    description = models.TextField(default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    