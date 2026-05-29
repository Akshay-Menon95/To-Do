from django.shortcuts import render,redirect
from rest_framework.decorators import api_view, permission_classes
from .models import todo
from .serializer import task_serializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.http import request
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated




# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def todo_list(request):
    a=todo.objects.filter(user=request.user)
    b= task_serializer(a,many=True)
    return Response(b.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def todocreate(request):
    a=task_serializer(data=request.data)
    if a.is_valid():
        a.save(user=request.user)
        return Response(a.data)
    return Response(a.errors)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def todoupdate(request,k):
    a=todo.objects.get(id=k)
    b=task_serializer(instance=a,data=request.data)
    if b.is_valid():
        b.save(user=request.user)
        return Response(b.data)
    return Response(b.errors)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def todopatch(request,k):
    a=todo.objects.get(id=k)
    b=task_serializer(a,data=request.data,partial=True)
    if b.is_valid():
        b.save(user=request.user)
        return Response(b.data)
    return Response(b.errors)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def tododelete(request,k):
    a=todo.objects.get(id=k,user=request.user)
    a.delete()
    return Response('Deleted successfully')

@api_view(['POST'])
def registerpage(request):
    a=request.data.get('username')
    b=request.data.get('password')
    User.objects.create_user(username=a,password=b)
    return Response({"User created successfully"})

@api_view(['POST'])
def loginpage(request):
    a=request.data.get('username')
    b=request.data.get('password')
    c=authenticate(username=a,password=b)
    if c:
        refresh=RefreshToken.for_user(c)
        return Response ({"refresh":str(refresh),'access':str(refresh.access_token)})
    