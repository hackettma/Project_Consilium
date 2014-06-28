from django.db import models

class Project(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100, blank=True, default='')
	description = models.TextField()
	author = models.CharField(max_length=100, blank=True, default='')

	class Meta:
		ordering = ('created',)