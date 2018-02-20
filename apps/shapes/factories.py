from factory import DjangoModelFactory

from apps.shapes.models import Shape, ShapeAttribute, ShapeAttributeValue


class ShapeFactory(DjangoModelFactory):
    class Meta:
        model = Shape


class ShapeAttributeFactory(DjangoModelFactory):
    class Meta:
        model = ShapeAttribute


class ShapeAttributeValueFactory(DjangoModelFactory):
    class Meta:
        model = ShapeAttributeValue
