from rest_framework.views import APIView
from . serializers import SigninSerializer, UserUpdateSerializer, UserListSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import get_object_or_404
from . models import User
# Create your views here.

class signin(APIView):
    def post(self,request):
        serializer = SigninSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response ("회원가입 완료",status=status.HTTP_200_OK)
        else:
            return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class UserUpdate(APIView):
    def put(self,request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user.id == user.id:
            serializer = UserUpdateSerializer(user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response (serializer.data, status=status.HTTP_200_OK)
            else:
                return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response('권한이 없습니다.', status=status.HTTP_400_BAD_REQUEST)

class UserDelete(APIView):
    def delete(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        if request.user.id == user.id:
            user.delete()
            return Response("탈퇴 완료!", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
        
class UserList(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserListSerializer(user, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)