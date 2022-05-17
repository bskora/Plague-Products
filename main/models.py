from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateField(auto_now=True)
    # body = models.TextField()
    body = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.title + " | " + str(self.date)