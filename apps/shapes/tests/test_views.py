from django.test import TestCase, Client
from django.urls import reverse

from ..factories import ShapeFactory


class TestShapeViewSet(TestCase):
    def setUp(self):
        self.client = Client()
        ShapeFactory.create(vertices=3)
        ShapeFactory.create(vertices=4)

    def test_list_returns_200(self):
        response = self.client.get(reverse('shapes:shape_list'))
        self.assertEqual(response.status_code, 200)

    def test_list_returns_all_shapes(self):
        response = self.client.get(reverse('shapes:shape_list'))
        self.assertEqual(len(response.data), 2)

    def test_list_returns_serialized_shapes(self):
        response = self.client.get(reverse('shapes:shape_list'))
        self.assertTrue(set(
            {'shape_name': 'triangle', 'vertices': 3}.items()).
            issubset(set(response.data[0].items())),
        )
