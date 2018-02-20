from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_201_CREATED

from ..models import Shape
from ..factories import ShapeFactory


class TestShapeViewSet(TestCase):
    def setUp(self):
        self.client = Client()
        self.shape_1 = ShapeFactory.create(vertices=3)
        ShapeFactory.create(vertices=4)

    def test_list_returns_200(self):
        response = self.client.get(reverse('shapes:shape-list'))
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_list_returns_all_shapes(self):
        response = self.client.get(reverse('shapes:shape-list'))
        self.assertEqual(len(response.data), 2)

    def test_list_returns_serialized_shapes(self):
        response = self.client.get(reverse('shapes:shape-list'))
        self.assertTrue(set(
            {'shape_name': 'triangle', 'vertices': 3}.items()).
            issubset(set(response.data[0].items())),
        )

    def test_detail_returns_404_for_invalid_id(self):
        response = self.client.get(
            reverse('shapes:shape-detail', kwargs={'pk': 999}),
        )
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_detail_returns_200_for_valid_id(self):
        response = self.client.get(
            reverse('shapes:shape-detail', kwargs={'pk': self.shape_1.id}),
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_detail_returns_serialized_shape_for_valid_id(self):
        response = self.client.get(
            reverse('shapes:shape-detail', kwargs={'pk': self.shape_1.id}),
        )
        self.assertTrue(set(
            {'shape_name': 'triangle', 'vertices': 3}.items()).
            issubset(set(response.data.items())),
        )

    def test_create_route_returns_201_for_valid_data(self):
        response = self.client.post(
            reverse('shapes:shape-list'),
            {'vertices': 4, 'name': 'test'},
        )
        self.assertEqual(response.status_code, HTTP_201_CREATED)

    def test_create_route_creates_a_shape(self):
        response = self.client.post(
            reverse('shapes:shape-list'),
            {'vertices': 4, 'name': 'test square'},
        )

        shape = Shape.objects.get(name='test square')

        self.assertEqual(shape.id, response.data['id'])



