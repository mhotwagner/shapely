from django.contrib import admin

from .models import Shape, ShapeAttribute, ShapeAttributeValue


class ShapeAdmin(admin.ModelAdmin):
    fields = (
        ('name', 'vertices'),
        'attributes',
    )


class ShapeAttributeAdmin(admin.ModelAdmin):
    fields = (
        'name', 'type', 'values'
    )


class ShapeAttributeValueAdmin(admin.ModelAdmin):
    fields = (
        'string_value', 'type',
    )


admin.site.register(Shape, ShapeAdmin)
admin.site.register(ShapeAttribute, ShapeAttributeAdmin)
admin.site.register(ShapeAttributeValue, ShapeAttributeValueAdmin)
