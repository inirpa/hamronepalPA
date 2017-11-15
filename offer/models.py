from django.db import models
from django.core.urlresolvers import reverse

class BookOffer(models.Model):
	name = models.CharField(max_length = 20)
	email =  models.EmailField(max_length = 50)
	nationality = models.CharField(max_length = 20)
	# package_type = models.ChoiceField()


