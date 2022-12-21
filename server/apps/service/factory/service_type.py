"""ServiceType Factory"""

# Thirdparty Libraries
import factory

# Own Libraries
from server.apps.service.models.service_type import ServiceType


class ServiceTypeFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = ServiceType

    name = factory.Faker("job")
