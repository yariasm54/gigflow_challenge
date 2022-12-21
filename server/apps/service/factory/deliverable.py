"""Deliverable Factory"""

# Thirdparty Libraries
import factory
import factory.fuzzy

# Own Libraries
from server.apps.service.models.package import Package
from server.apps.service.models.deliverable import Deliverable


class DeliverableFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Deliverable

    name = factory.Faker("sentence", nb_words=10)
    package = factory.Iterator(Package.objects.all())
