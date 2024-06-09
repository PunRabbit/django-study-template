from rest_framework import viewsets, mixins

from app.model.snippet import Snippet as SnippetModel
from app.serializer.snippet import Snippet as SnippetSerializer


class UserListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = SnippetModel.objects.all()
    serializer_class = SnippetSerializer
