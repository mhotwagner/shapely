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
