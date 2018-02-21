from distutils.util import strtobool

from django.db import models, IntegrityError
from django_extensions.db.fields import AutoSlugField

from apps.common.utils import dynamicdefaultdict


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

    name = models.CharField(max_length=64)
    vertices = models.IntegerField(null=False)
    attributes = models.ManyToManyField('ShapeAttribute', related_name='shapes', null=True)

    @property
    def shape_name(self):
        return self.SHAPE_NAMES[self.vertices]

    def __str__(self):
        if self.name:
            return '{}:{}'.format(self.name, self.shape_name)
        else:
            return self.shape_name


STRING = 'string'
INTEGER = 'integer'
BOOLEAN = 'boolean'
SHAPE_ATTRIBUTE_TYPES = (
    (STRING, 'STRING'),
    (INTEGER, 'INTEGER'),
    (BOOLEAN, 'BOOLEAN'),
)


class ShapeAttribute(models.Model):
    name = models.CharField(max_length=16)
    type = models.CharField(max_length=8, choices=SHAPE_ATTRIBUTE_TYPES, default=STRING)
    values = models.ManyToManyField('ShapeAttributeValue', related_name='attributes')

    def save(self, *args, **kwargs):
        if self.name == '':
            raise IntegrityError('name cannot be blank')
        super(ShapeAttribute, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class ShapeAttributeValue(models.Model):
    TYPE_CASTER = {
        STRING: lambda x: str(x),
        INTEGER: lambda x: int(x),
        BOOLEAN: lambda x: bool(strtobool(x)),
    }

    string_value = models.CharField(max_length=64)
    slug = AutoSlugField(populate_from=string_value)
    type = models.CharField(max_length=8, choices=SHAPE_ATTRIBUTE_TYPES, default=STRING)

    @property
    def value(self):
        return self.TYPE_CASTER[self.type](self.string_value)

    def save(self, *args, **kwargs):
        try:
            self.TYPE_CASTER[self.type](self.string_value)
        except ValueError:
            raise IntegrityError('"{}" cannot be cast to type {}'.format(
                self.string_value, self.type,
            ))

        super(ShapeAttributeValue, self).save(*args, **kwargs)

    def __str__(self):
        return self.value
