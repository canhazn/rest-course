from snippets.models import Snippet
from snippets.serializers import SnippetSerializer
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


class SnippetsList(APIView):
    """
    List all code snippets, or create a new snippet
    """

    def get(self, request, format=None):
        snippets = Snippet.objects.all()
        serializer = SnippetSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = JSONParser().parse(request)
        print(data)
        serializer = SnippetSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SnippetDetail(APIView):
    """
    Retrive, update or delete a code snippet
    """

    def get_object(self, pk):
        try:
            return Snippet.objects.get(pk=pk)
        except Snippet.DesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        snippet = self.get_object(pk)
        serialiezer = SnippetSerializer(snippet)
        return Response(serialiezer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = SnippetSerializer(snippet, request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
