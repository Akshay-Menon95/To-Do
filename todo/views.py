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

@api_view(['POST'])
def todocreate(request):
    a=task_serializer(data=request.data)
    if a.is_valid():
        a.save()
        return Response(a.data)
    return Response(a.errors)

@api_view(['PUT'])
def todoupdate(request,pk):
    a=todo.objects.get(id=pk)
    b=task_serializer(instance=a,data=request.data)
    if b.is_valid():
        b.save()
        return Response(b.data)
    return Response(b.errors)
