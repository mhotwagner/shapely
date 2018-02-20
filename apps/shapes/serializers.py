from rest_framework import serializers

from .models import Shape, ShapeAttribute, ShapeAttributeValue


class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = (
            'id',
            'shape_name',
        )


class ShapeAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShapeAttribute
        fields = (
            'id',
            'name',
            'type',
        )


class ShapeAttributeValueSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShapeAttributeValue
        fields = (
            'id',
            'string_value',
            'value',
            'type',
        )
