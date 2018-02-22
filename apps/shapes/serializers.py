from rest_framework import serializers

from .models import Shape, ShapeAttribute, ShapeAttributeValue


def greater_than_two(value):
    if value < 3:
        raise serializers.ValidationError('This field must be 3 or greater.')


class ShapeSerializer(serializers.ModelSerializer):
    vertices = serializers.IntegerField(validators=(greater_than_two,))

    class Meta:
        model = Shape
        fields = (
            'id',
            'name',
            'shape_name',
            'vertices',
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
