"""Deliverable Serializer."""

# Thirdparty Libraries
from rest_framework import serializers

# Own Libraries
from server.apps.service.models import Deliverable


class DeliverableSerializer(serializers.ModelSerializer):
    """Deliverable model serializer.

    Args:
        ModelSerializer: provides a shortcut that lets you automatically create a
        serializer class with fields that correspond to the Model fields.

    Returns:
        a serialized data of the Deliverable.
    """

    class Meta:
        model = Deliverable
        fields = ['id', 'name']
