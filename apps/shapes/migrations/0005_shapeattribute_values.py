# Generated by Django 2.0.2 on 2018-02-20 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0004_shapeattributevalue'),
    ]

    operations = [
        migrations.AddField(
            model_name='shapeattribute',
            name='values',
            field=models.ManyToManyField(related_name='attributes', to='shapes.ShapeAttributeValue'),
        ),
    ]
