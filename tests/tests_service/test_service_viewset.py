"""Service type test viewsets."""

# Standard Libraries
import random

# Thirdparty Libraries
from rest_framework import status
from rest_framework.test import APITestCase

# Own Libraries
from server.apps.service.factory.package import PackageFactory
from server.apps.service.factory.deliverable import DeliverableFactory
from server.apps.service.factory.service_type import ServiceTypeFactory


DEFAULT_VALUE = 100


class ServiceTestCase(APITestCase):
    """Service Test Case, test endpoint that exposes the list of service types.

    Args:
        APITestCase: Test case class included in the REST framework.
    """
    url = '/api/v1/'

    def test_list_services(self):
        """
        Test prepared to check the response of the service GET 'services/'
        """

        # Create records in the database
        for count in range(DEFAULT_VALUE):
            ServiceTypeFactory.create()

        response = self.client.get(
            self.url + 'services/',
            format='json'
        )
        # import pdb;pdb.set_trace()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), DEFAULT_VALUE)

    def test_search_service(self):
        """
        Test prepared to check the response of the service GET 'services/{id}'.
        """

        # Create record in the database
        service_id = ServiceTypeFactory.create()

        # Make request with a created service type ID
        id_search = service_id.id
        response = self.client.get(
            self.url + f'services/{str(id_search)}/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_service_error(self):
        """
        Test prepared to check the response of the service GET 'services/{id}'
        when the id is not created.
        """

        # Make request with a service type ID without created
        id_search = 9874485123
        response = self.client.get(
            self.url + f'services/{str(id_search)}/',
            format='json'
        )

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response.data['detail'], 'Not found.')

