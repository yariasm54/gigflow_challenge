"""Package Serializer."""

# Thirdparty Libraries
from rest_framework import serializers

# Own Libraries
from server.apps.service.models import Package
from server.apps.service.serializers.deliverable import DeliverableSerializer


class PackageSerializer(serializers.ModelSerializer):
    """Package model serializer.

    Args:
        ModelSerializer: provides a shortcut that lets you automatically create a
        serializer class with fields that correspond to the Model fields.

    Returns:
        a serialized data of the Package.
    """

    deliverables = DeliverableSerializer(many=True, read_only=True)
    price = serializers.FloatField()
    typeOfServiceID = serializers.IntegerField(source="service_type.id")

    class Meta:
        model = Package
        fields = ['id', 'description', 'price', 'typeOfServiceID', 'deliverables']
