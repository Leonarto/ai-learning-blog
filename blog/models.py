from django.db import models
from core.models import BaseModel


class BlogPage(BaseModel):
    url_path = models.CharField(max_length=500, null=True, unique=True)
    markdown = models.TextField(null=True)

