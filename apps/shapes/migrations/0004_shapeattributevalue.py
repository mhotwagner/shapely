# Generated by Django 2.0.2 on 2018-02-20 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0003_shape_attributes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShapeAttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string_value', models.CharField(max_length=64)),
                ('type', models.CharField(choices=[('string', 'STRING')], default='string', max_length=8)),
            ],
        ),
    ]
