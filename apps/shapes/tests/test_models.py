from django.db import IntegrityError
from django.test import TestCase
from factory import DjangoModelFactory

from ..models import Shape, ShapeAttribute


class ShapeFactory(DjangoModelFactory):
    class Meta:
        model = Shape


class ShapeAttributeFactory(DjangoModelFactory):
    class Meta:
        model = ShapeAttribute


class TestShapeModel(TestCase):
    def test_a_shape_cannot_be_created_without_vertices(self):
        with self.assertRaises(IntegrityError):
            ShapeFactory.create()

    def test_a_shape_can_be_created_with_vertices(self):
        shape = ShapeFactory.create(vertices=3)

        fetched_shape = Shape.objects.get(id=shape.id)

        self.assertIsNotNone(fetched_shape.id)
        self.assertEqual(shape, fetched_shape)

    def test_a_shape_with_3_vertices_has_shape_name_triangle(self):
        triangle = ShapeFactory.create(vertices=3)

        self.assertEqual(triangle.shape_name, 'triangle')

    def test_a_shape_with_11_vertices_has_shape_name_11_gon(self):
        shape = ShapeFactory.create(vertices=11)

        self.assertEqual(shape.shape_name, '11-gon')

    def test_a_shape_can_have_attributes(self):
        shape_attribute_1 = ShapeAttributeFactory(name='one')
        shape_attribute_2 = ShapeAttributeFactory(name='two')
        shape = ShapeFactory.create(vertices=3)
        shape.attributes.add(shape_attribute_1, shape_attribute_2)

        self.assertEqual(shape.attributes.count(), 2)


class TestShapeAttributeModel(TestCase):
    def setUp(self):
        self.shape = ShapeFactory(vertices=3)

    def test_a_shape_attribute_cannot_be_created_without_a_name(self):
        with self.assertRaises(IntegrityError):
            ShapeAttributeFactory.create()

    def test_a_shape_attribute_can_be_created_with_valid_inputs(self):
        shape_attribute = ShapeAttributeFactory.create(name='an attribute')

        fetched_shape_attribute = ShapeAttribute.objects.get(name='an attribute')

        self.assertIsNotNone(fetched_shape_attribute.id)
        self.assertEqual(shape_attribute, fetched_shape_attribute)

    def test_a_shape_can_be_added_to_a_shape_attribute(self):
        shape_attribute = ShapeAttributeFactory.create(name='an attribute')
        shape_attribute.shapes.add(self.shape)

        self.assertEqual(shape_attribute.shapes.count(), 1)
