from django.test import TestCase

from ..factories import ShapeFactory, ShapeAttributeFactory
from ..serializers import ShapeSerializer, ShapeAttributeSerializer


class TestShapeSerializer(TestCase):
    def test_it_can_serialize_a_shape(self):
        shape = ShapeFactory.create(vertices=3)

        serializer = ShapeSerializer(shape)

        self.assertIsNotNone(serializer.data['id'])
        self.assertEqual(serializer.data['shape_name'], 'triangle')


class TestShapeAttributeSerializer(TestCase):
    def test_it_can_serialize_a_shape_attribute(self):
        shape_attribute = ShapeAttributeFactory.create(name='color')

        serializer = ShapeAttributeSerializer(shape_attribute)

        self.assertIsNotNone(serializer.data['id'])
        self.assertEqual(serializer.data['name'], 'color')
        self.assertEqual(serializer.data['type'], 'string')

