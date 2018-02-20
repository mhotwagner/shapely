from rest_framework.viewsets import ModelViewSet

from .serializers import ShapeSerializer
from .models import Shape


class ShapeViewSet(ModelViewSet):
    queryset = Shape.objects.all()
    serializer_class = ShapeSerializer
