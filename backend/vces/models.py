from django.db import models

class VCE(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    file = models.ImageField(upload_to='vces')

    def __str__(self):
        return self.title