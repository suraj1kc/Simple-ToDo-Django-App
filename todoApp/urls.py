from django.urls import path
from . views import home, addTodo, editTodo, deleteTodo

urlpatterns = [
    path('', home.as_view(), name='home'),
    path('add-todo/', addTodo.as_view(), name='add_todo'),
    path('delete-todo/<int:id>/', deleteTodo.as_view(), name='delete_todo'),
    path('edit-todo/<int:id>/', editTodo.as_view(), name='edit_todo'),
]
