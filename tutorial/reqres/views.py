from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from tutorial.reqres.models import Snippet
from tutorial.reqres.serializers import SnippetModelSerializer


@api_view(['GET', 'POST'])
def snippet_list(request):
    if request.method == 'GET':
        snippets = Snippet.objects.all()
        serializer = SnippetModelSerializer(snippets, many=True)

