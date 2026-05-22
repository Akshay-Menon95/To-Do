from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import todo
from .serializer import task_serializer
from rest_framework.response import Response


# Create your views here.
@api_view(['GET'])
def todo_list(request):
    a=todo.objects.all()
    b= task_serializer(a,many=True)
    return Response(b.data)