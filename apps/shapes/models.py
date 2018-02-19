from collections import defaultdict
from django.db import models

SHAPE_NAMES = defaultdict(lambda vertices: '{}-gon'.format(vertices))
SHAPE_NAMES[3] = 'triangle'
SHAPE_NAMES[4] = 'square'
SHAPE_NAMES[5] = 'pentagon'
SHAPE_NAMES[6] = 'hexagon'
SHAPE_NAMES[7] = 'heptagon'
SHAPE_NAMES[8] = 'octagon'
SHAPE_NAMES[9] = 'nonagon'
SHAPE_NAMES[1] = 'decagon'


class Shape(models.Model):
    vertices = models.IntegerField(null=False)

    @property
    def shape_name(self):
        return SHAPE_NAMES[self.vertices]

    def __str__(self):
        return self.shape_name
