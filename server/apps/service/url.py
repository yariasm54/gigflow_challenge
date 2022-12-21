"""Service URLs."""

# Django Libraries
from django.urls import include, path

# Own Libraries
from rest_framework.routers import SimpleRouter
from server.apps.service.viewsets.service import ServiceTypeViewSet

router = SimpleRouter()
router.register(r"", ServiceTypeViewSet, basename="service")

urlpatterns = [
    path("services/", include(router.urls)),
]
