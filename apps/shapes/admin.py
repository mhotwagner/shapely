from django.contrib import admin

from .models import Shape


class ShapeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Shape, ShapeAdmin)
