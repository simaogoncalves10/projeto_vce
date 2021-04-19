from django.db import models


class Endoscopy(models.Model):
	name = models.CharField(max_length=50, null=False, blank=True)
	

class Image(models.Model):
	name = models.CharField(max_length=50, null=False, blank=True)
	image = models.ImageField(upload_to="images", null=False, blank=True)
	id_endoscopy = models.ForeignKey(Endoscopy, on_delete=models.CASCADE, default = None) 

	def __str__(self):
		return self.name