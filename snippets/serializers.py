from rest_framework import serializers
from snippets.models import Snippet


class SnippetSerializer(serializers.Serializer):
    class Meta:
        model = Snippet
        fields = '__all__'
