from django.db import IntegrityError
from django.test import TestCase
from factory import DjangoModelFactory

from .models import Shape


class ShapeFactory(DjangoModelFactory):
    class Meta:
        model = Shape


class TestShapeModel(TestCase):
    def test_a_shape_cannot_be_created_without_vertices(self):
        with self.assertRaises(IntegrityError):
            ShapeFactory.create()

    def test_a_shape_can_be_created_with_vertices(self):
        shape = ShapeFactory.create(vertices=3)

        fetched_shape = Shape.objects.get(id=shape.id)

        self.assertEqual(shape, fetched_shape)

    def test_a_shape_with_3_vertices_has_shape_name_triangle(self):
        triangle = ShapeFactory.create(vertices=3)

        self.assertEqual(triangle.shape_name, 'triangle')

    def test_a_shape_with_11_vertices_has_shape_name_11_gon(self):
        shape = ShapeFactory.create(vertices=11)

        self.assertEqual(shape.shape_name, '11-gon')
