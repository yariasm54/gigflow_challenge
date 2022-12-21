"""Service type viewsets."""

# Thirdparty Libraries
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Own Libraries
from server.apps.service.models import ServiceType
from server.apps.service.serializers.service import ServiceTypeSerializer


class ServiceTypeViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    """A viewset for retrieving or list a Service type objects.

    Args:
        RetrieveModelMixin: Return a Service type instance
        ListModelMixin: Return all topics, ordered by name
        GenericViewSet: include the base set of generic view behavior,
        such as the `get_object` and `get_queryset` methods

    Returns:
        Service type object
    """

    serializer_class = ServiceTypeSerializer
    permission_classes = ()
    pagination_class = None

    def get_queryset(self):
        return ServiceType.objects.all()

    def list(self, request):
        queryset = ServiceType.objects.prefetch_related('packages')
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = ServiceType.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user)
        return Response(serializer.data)
