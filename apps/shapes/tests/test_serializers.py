from django.test import TestCase

from ..factories import ShapeFactory
from ..serializers import ShapeSerializer


class TestShapeSerializer(TestCase):
    def test_it_can_serialize_a_shape_(self):
        shape = ShapeFactory.create(vertices=3)

        serializer = ShapeSerializer(shape)

        self.assertIsNotNone(serializer.data['id'])
        self.assertEqual(serializer.data['shape_name'], 'triangle')