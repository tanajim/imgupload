from django.db import models

# Create your models here.
class Imguploading(models.Model):
    uname = models.CharField(blank=False,max_length=50,null=False)
    profile = models.ImageField(upload_to=None, height_field=None, width_field=None)

    def __str__(self):
        return self.uname