from django.db import models

class AL(models.Model):
    name = models.CharField(max_length=50, null=False, blank=True)
    n_instances = models.IntegerField(null=False, default=10)
    accuracy_goal = models.FloatField(null=False, default=85)