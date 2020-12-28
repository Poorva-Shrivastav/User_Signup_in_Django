from django.db import models

from django.urls import reverse

import uuid

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=20, )
	last_name = models.CharField(max_length=20)
	email = models.CharField(max_length=50, default=uuid.uuid4)


	def get_absolute_url(self):
	 	return reverse("signuperror:signup-detail", kwargs={"id": self.id}) 
