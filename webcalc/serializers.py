from django.forms import widgets
from rest_framework import serializers


class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('id', 'created', 'title', 'author')

"""
class ProjectSerializer(serializers.Serializer):
	pk = serializers.Field()
	title = serializers.CharField(required=False, max_length=100)
	description = serializers.CharField(widget=widgets.Textarea, max_length=10000)
	author = serializers.CharField(required=False, max_length=100)

	def restore_object(self, attrs, instance=None):
		if instance:
			instance.title = attrs.get('title', instance.title)
			instance.description = attrs.get('description', instance.description)
			instance.author = attrs.get('author', instance.author)

			return instance
"""