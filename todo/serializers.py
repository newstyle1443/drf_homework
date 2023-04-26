from rest_framework import serializers
from . models import Todo

class TodoListSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.email
    
    class Meta:
        model = Todo
        fields = "__all__"

class CreateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title',)

class UpdateTodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ("title", "is_complete",)