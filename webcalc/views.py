from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from webcalc.models import Project
from webcalc.serializers import ProjectSerializer
# Create your views here.


class JSONResponse(HttpResponse):
	"""
	An HttpResponse that renders its content into JSON.
	"""
	def __init__(self, data, **kwargs):
		content = JSONRenderer().render(data)
		kwargs['content_type'] = 'application/json'
		super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def project_list(request):
	"""	List all projects or create a new projects"""
	if request.method == 'GET':
		projects = Project.objects.all()
		serializer = ProjectSerializer(projects, many=True)
		return JSONResponse(serializer.data)

	elif request.method == 'POST':
		data = JSONParser().parse(request)
		serializer = ProjectSerializer(data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data, status=201)
		return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def project_detail(request, pk):
	"""
	Retrieve, update or delete a Project.
	"""
	try:
		project = Project.objects.get(pk=pk)
	except Project.DoesNotExist:
		return HttpResponse(status=404)

	if request.method == 'GET':
		serializer = ProjectSerializer(project)
		return JSONResponse(serializer.data)

	elif request.method == 'PUT':
		data = JSONParser().parse(request)
		serializer = ProjectSerializer(project, data=data)
		if serializer.is_valid():
			serializer.save()
			return JSONResponse(serializer.data)
		return JSONResponse(serializer.errors, status=400)

	elif request.method == 'DELETE':
		project.delete()
		return HttpResponse(status=204)