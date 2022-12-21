"""Package Factory"""

# Standard Libraries
from typing import Final

# Thirdparty Libraries
import factory
import factory.fuzzy

# Own Libraries
from server.apps.service.models.package import Package
from server.apps.service.models.service_type import ServiceType


MIN_PRICE: Final = 100
MAX_PRICE: Final = 5000


class PackageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Package

    description = factory.Faker("sentence", nb_words=10)
    price = factory.fuzzy.FuzzyDecimal(low=MIN_PRICE, high=MAX_PRICE)
    service_type = factory.Iterator(ServiceType.objects.all())
