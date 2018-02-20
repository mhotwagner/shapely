from django.db import models, IntegrityError

from apps.common.utils import dynamicdefaultdict


class ShapeAttribute(models.Model):
    STRING = 'string'
    SHAPE_ATTRIBUTE_TYPES = (
        (STRING, 'STRING'),
    )

    name = models.CharField(max_length=16)
    type = models.CharField(max_length=8, choices=SHAPE_ATTRIBUTE_TYPES, default=STRING)
    
    def save(self, *args, **kwargs):
        if self.name == '':
            raise IntegrityError('name cannot be blank')
        super(ShapeAttribute, self).save(*args, **kwargs)


class Shape(models.Model):
    SHAPE_NAMES = dynamicdefaultdict(lambda vertices: '{}-gon'.format(vertices))
    SHAPE_NAMES[3] = 'triangle'
    SHAPE_NAMES[4] = 'square'
    SHAPE_NAMES[5] = 'pentagon'
    SHAPE_NAMES[6] = 'hexagon'
    SHAPE_NAMES[7] = 'heptagon'
    SHAPE_NAMES[8] = 'octagon'
    SHAPE_NAMES[9] = 'nonagon'
    SHAPE_NAMES[1] = 'decagon'

    vertices = models.IntegerField(null=False)

    @property
    def shape_name(self):
        return self.SHAPE_NAMES[self.vertices]

    def __str__(self):
        return self.shape_name
