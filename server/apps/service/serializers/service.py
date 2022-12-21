"""Service type Serializer."""

# Thirdparty Libraries
from rest_framework import serializers

# Own Libraries
from server.apps.service.models import ServiceType
from server.apps.service.serializers.package import PackageSerializer


class ServiceTypeSerializer(serializers.ModelSerializer):
    """Service type model serializer.

    Args:
        ModelSerializer: provides a shortcut that lets you automatically create a
        serializer class with fields that correspond to the Model fields.

    Returns:
        a serialized data of the Service type.
    """

    packages = PackageSerializer(many=True, read_only=True)

    class Meta:
        """Meta class."""

        model = ServiceType
        fields = [
            "id",
            "name",
            "packages",
        ]