from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import TodoSerializer, TodoToggleCompleteSerializer
from todo.models import Todo


class TodoListAndCreate(APIView):
    """对返回格式进行了简单的定制，需要使用 APIView，
    因为默认的返回格式是列表，而列表中的每个元素都是字典
    """
    def get(self, request):
        # user = request.user
        # todos = Todo.objects.filter(user=user).order_by('-created')
        todos = Todo.objects.all().order_by('-created')
        serializer = TodoSerializer(todos, many=True)
        return Response({"items": serializer.data})

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response({"error": serializer.errors}, status=400)


class TodoToggleComplete(generics.UpdateAPIView):
    serializer_class = TodoToggleCompleteSerializer
    queryset = Todo.objects.all()

    def perform_update(self, serializer):
        serializer.instance.completed = not (serializer.instance.completed)
        serializer.save()


# class TodoListCreate(generics.ListCreateAPIView):
#     serializer_class = TodoSerializer
#     # permission_classes = [permissions.IsAuthenticated]

#     def get_queryset(self):
#         # user = self.request.user
#         # return Todo.objects.filter(user=user).order_by('-created')
#         limit = self.request.query_params.get('Limit', None)
#         if limit is None:
#             return Todo.objects.filter().order_by('-created')
#         else:
#             return Todo.objects.filter().order_by('-created')[:int(limit)]

#     def perform_create(self, serializer):
#         # serializer holds a django model
#         # serializer.save(user=self.request.user)
#         serializer.save()


class TodoRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # user = self.request.user
        # user can only update, delete own posts
        # return Todo.objects.filter(user=user)
        return Todo.objects.filter()


# class TodoToggleComplete(generics.UpdateAPIView):
#     serializer_class = TodoToggleCompleteSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#
#     def get_queryset(self):
#         user = self.request.user
#         return Todo.objects.filter(user=user)
#
#     def perform_update(self, serializer):
#         serializer.instance.completed = not (serializer.instance.completed)
#         serializer.save()
