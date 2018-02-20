import json

from django.test import TestCase, Client
from django.urls import reverse
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND,
)

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

    def test_update_route_returns_400_with_only_partial_data(self):
        shape = ShapeFactory.create(vertices=3)
        response = self.client.put(
            reverse('shapes:shape-detail', kwargs={'pk': shape.id}),
            json.dumps({'vertices': 4}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, HTTP_400_BAD_REQUEST)

    def test_update_route_returns_200_with_all_data(self):
        shape = ShapeFactory.create(vertices=3)
        response = self.client.put(
            reverse('shapes:shape-detail', kwargs={'pk': shape.id}),
            json.dumps({'vertices': 4, 'name': 'test'}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, 200)

    def test_update_route_updates_object(self):
        shape = ShapeFactory.create(vertices=3)
        self.client.put(
            reverse('shapes:shape-detail', kwargs={'pk': shape.id}),
            json.dumps({'vertices': 4, 'name': 'test'}),
            content_type='application/json',
        )
        fetched_shape = Shape.objects.get(id=shape.id)
        self.assertEqual(fetched_shape.vertices, 4)

    def test_partial_update_route_returns_200_with_valid_partial_data(self):
        shape = ShapeFactory.create(vertices=3)
        response = self.client.patch(
            reverse('shapes:shape-detail', kwargs={'pk': shape.id}),
            json.dumps({'vertices': 4}),
            content_type='application/json',
        )
        self.assertEqual(response.status_code, HTTP_200_OK)

    def test_delete_route_returns_400_for_invalid_id(self):
        response = self.client.delete(reverse('shapes:shape-detail', kwargs={'pk': 999}))
        self.assertEqual(response.status_code, HTTP_404_NOT_FOUND)

    def test_delete_route_returns_400_for_invalid_id(self):
        shape = ShapeFactory.create(vertices=3)
        response = self.client.delete(reverse('shapes:shape-detail', kwargs={'pk': shape.id}))
        self.assertEqual(response.status_code, HTTP_204_NO_CONTENT)

    def test_delete_route_deletes_object(self):
        shape = ShapeFactory.create(vertices=3)
        self.client.delete(reverse('shapes:shape-detail', kwargs={'pk': shape.id}))
        with self.assertRaises(Shape.DoesNotExist):
            Shape.objects.get(id=shape.id)

