from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . serializers import CreateTodoSerializer,TodoListSerializer, UpdateTodoSerializer
from rest_framework import status
from rest_framework.generics import get_object_or_404
from . models import Todo
from datetime import datetime
from users.models import User

# Create your views here.

class TodoList(APIView):
    def get(self,request):
            list = Todo.objects.all()
            serializer = TodoListSerializer(list, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
    
class CreateTodo(APIView):
    def post(self,request):
        serializer = CreateTodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UpdateTodo(APIView):
    def put(self,request,todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            serializer = UpdateTodoSerializer(todo, data=request.data)
            if serializer.is_valid():
                if request.data['is_complete'] == 'true':
                    todo.completion_at = datetime.today()
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
class DeleteTodo(APIView):
    def delete(self, request,todo_id):
        todo = get_object_or_404(Todo, id=todo_id)
        if request.user == todo.user:
            todo.delete()
            return Response("삭제완료", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response('권한이 없습니다.', status=status.HTTP_403_FORBIDDEN)
    