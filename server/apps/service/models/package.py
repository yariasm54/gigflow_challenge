"""Service.package app data model."""

# Standard Libraries
from typing import Final

# Django Libraries
from django.db import models


MAX_MOUNT_DIGITS: Final = 15
MAX_LENGTH_CHAR_FIELD: Final = 255


class Package(models.Model):
    """Package stores packages."""

    description = models.CharField(
        verbose_name="Description",
        max_length=MAX_LENGTH_CHAR_FIELD,
        help_text="Package description",
    )
    price = models.DecimalField(
        max_digits=MAX_MOUNT_DIGITS,
        decimal_places=2,
        verbose_name="Price",
        help_text="Package price",
        default=0,
    )
    service_type = models.ForeignKey(
        "service.ServiceType",
        verbose_name="Service type",
        on_delete=models.PROTECT,
        help_text="Package service type",
        related_name='packages',
    )

    class Meta:
        """Meta."""

        verbose_name = "Package"
        verbose_name_plural = "Packages"

    def __str__(self):
        """__str__ Method to return a human-readable identifier of the object.

        String of characters that is the attribute 'description' and identifies in a
        human readable form a packages.

        :return: String of characters that is the attribute 'description'
        :rtype: str
        """
        return f"{self.description}"
