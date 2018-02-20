from django.db import IntegrityError
from django.test import TestCase

from ..factories import ShapeFactory, ShapeAttributeFactory, ShapeAttributeValueFactory
from ..models import (
    Shape, ShapeAttribute, ShapeAttributeValue,
    INTEGER, STRING,
)


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
        attribute = ShapeAttributeFactory.create(name='an attribute')

        fetched_attribute = ShapeAttribute.objects.get(name='an attribute')

        self.assertIsNotNone(fetched_attribute.id)
        self.assertEqual(attribute, fetched_attribute)

    def test_a_shape_attribute_can_have_values(self):
        value_1 = ShapeAttributeValueFactory.create(string_value='red')
        value_2 = ShapeAttributeValueFactory.create(string_value='blue')

        attribute = ShapeAttributeFactory(name='color')

        attribute.values.add(value_1, value_2)

        self.assertEqual(attribute.values.count(), 2)


class TestShapeAttributeValue(TestCase):
    def test_a_value_can_be_created(self):
        value = ShapeAttributeValueFactory.create()

        fetched_value = ShapeAttributeValue.objects.first()

        self.assertIsNotNone(fetched_value.id)
        self.assertEqual(value, fetched_value)

    def test_value_with_type_string_returns_a_string(self):
        value = ShapeAttributeValueFactory.create(string_value='some value')

        self.assertEqual(type(value.value), str)

    def test_value_with_type_integer_cannot_be_a_non_integer_string(self):
        with self.assertRaises(IntegrityError):
            ShapeAttributeValueFactory.create(
                string_value='some value',
                type=INTEGER,
            )

    def test_value_with_type_integer_returns_an_integer(self):
        value = ShapeAttributeValueFactory.create(
            string_value='999',
            type=INTEGER,
        )

        self.assertEqual(type(value.value), int)
        self.assertEqual(value.value, 999)
