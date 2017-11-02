from django.db import models

# Create your models here.
class BlogOption(models.Model):
	title = models.CharField(max_length = 50)
	site_logo = models.FileField(blank = True)
	header_banner = models.FileField(blank = True)
	favicon = models.FileField(blank = True)

	def save(self):
		count = BlogOption.objects.all().count()
		save_permission = BlogOption.has_add_permission(self)

		if(count < 1):
			super(BlogOption,self).save()
		elif save_permission:
			super(BlogOption,self).save()

	def has_add_permission(self):
		return BlogOption.objects.filter(id = self.id).exists()		


	def __str__(self):
		return self.title + ' - ' + str(self.site_logo)	+ ' - ' + str(self.header_banner) + ' - ' + str(self.favicon)


class Memo(models.Model):
	author = models.CharField(max_length = 50)
	description = models.TextField()
	featured_image = models.FileField(blank = True)

	def __str__(self):
		return self.author +' -- '+ self.description + ' -- ' + str(self.featured_image)