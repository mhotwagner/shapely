# Generated by Django 2.0.2 on 2018-02-20 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shapes', '0007_auto_20180220_0459'),
    ]

    operations = [
        migrations.AddField(
            model_name='shape',
            name='name',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]
