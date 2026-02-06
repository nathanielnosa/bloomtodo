from rest_framework import status,serializers
from rest_framework.views import APIView
from rest_framework.response import Response

from . models import Todo
from . serializers import TodoSerializer


# post, get, put, patch, delete

# CREATE
class CreateRetrieveView(APIView):
    # create
    def post(self,request):
        try:
            serializers = TodoSerializer(data=request.data)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response({serializers.errors},status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # fetch all todo
    def get(self,request):
        try:
            todo = Todo.objects.all()
            serializers = TodoSerializer(todo, many=True)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetUpdateDeleteView(APIView):
    # get
    def get(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializer(todo)
            return Response(serializers.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # update
    def put(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            serializers = TodoSerializer(todo,data=request.data,partial=True)
            if serializers.is_valid():
                serializers.save()
                return Response(serializers.data, status=status.HTTP_201_CREATED)
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # delete
    def delete(self,request,id):
        try:
            todo = Todo.objects.get(id=id)
            todo.delete()
            return Response({"Message":f"{todo.title} Deleted"}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"Error":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

