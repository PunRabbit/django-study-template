from rest_framework import viewsets, mixins


class UserListViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    pass
