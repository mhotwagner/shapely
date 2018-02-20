from rest_framework import serializers

from .models import Shape, ShapeAttribute


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