from django.urls import path

from . import views

urlpatterns = [
    # 自定义了一些字段，因此使用了 APIView
    path('todos', views.TodoListAndCreate.as_view()),
    # path('todos', views.TodoListCreate.as_view()),
    path('todos/<int:pk>', views.TodoRetrieveUpdateDestroy.as_view()),
    path('todos/<int:pk>/complete', views.TodoToggleComplete.as_view()),
]
