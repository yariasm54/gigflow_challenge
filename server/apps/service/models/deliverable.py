"""Service.deliverable app data model."""

# Standard Libraries
from typing import Final

# Django Libraries
from django.db import models


MAX_LENGTH_CHAR_FIELD: Final = 255


class Deliverable(models.Model):
    """Deliverable stores the deliverables of a package."""

    name = models.CharField(
        verbose_name="Name",
        max_length=MAX_LENGTH_CHAR_FIELD,
        help_text="Deliverable name",
    )
    package = models.ForeignKey(
        "service.Package",
        verbose_name="Package",
        on_delete=models.PROTECT,
        help_text="Package",
        related_name='deliverables',
    )

    class Meta:
        """Meta."""

        verbose_name = "Deliverable"
        verbose_name_plural = "Deliverables"

    def __str__(self):
        """__str__ Method to return a human-readable identifier of the object.

        String of characters that is the attribute 'name' and identifies in a
        human readable form a deliverables.

        :return: String of characters that is the attribute 'name'
        :rtype: str
        """
        return f"{self.name}"
