"""Service.service_type app data model."""

# Standard Libraries
from typing import Final

# Django Libraries
from django.db import models

MAX_LENGTH_CHAR_FIELD: Final = 255


class ServiceType(models.Model):
    """ServiceType stores service types."""

    name = models.CharField(
        verbose_name="Name",
        max_length=MAX_LENGTH_CHAR_FIELD,
        help_text="Service type name",
    )

    class Meta:
        """Meta."""

        verbose_name = "Service Type"
        verbose_name_plural = "Service Types"

    def __str__(self):
        """__str__ Method to return a human-readable identifier of the object.

        String of characters that is the attribute 'name' and identifies in a
        human readable form a type of service.

        :return: String of characters that is the attribute 'name'
        :rtype: str
        """
        return f"{self.name}"
