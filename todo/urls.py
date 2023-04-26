from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.TodoList.as_view(), name='todo_list'),
    path('create/', views.CreateTodo.as_view(), name='create_todo'),
    path('update/<int:todo_id>/', views.UpdateTodo.as_view(), name='update_todo'),
    path('delete/<int:todo_id>/', views.DeleteTodo.as_view(), name='delete_todo'),

]
