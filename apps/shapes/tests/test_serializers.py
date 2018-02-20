from django.test import TestCase

from ..factories import ShapeFactory, ShapeAttributeFactory, ShapeAttributeValueFactory
from ..models import INTEGER
from ..serializers import ShapeSerializer, ShapeAttributeSerializer, ShapeAttributeValueSerializer


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


class TestShapeAttributeValueSerializer(TestCase):
    def test_it_can_serialize_a_shape_attribute_value(self):
        shape_attribute_value = ShapeAttributeValueFactory.create(
            string_value='15', type=INTEGER,
        )

        serializer = ShapeAttributeValueSerializer(shape_attribute_value)

        self.assertIsNotNone(serializer.data['id'])
        self.assertEqual(serializer.data['string_value'], '15')
        self.assertEqual(serializer.data['value'], 15)
        self.assertEqual(serializer.data['type'], 'integer')

