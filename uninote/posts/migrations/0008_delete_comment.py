# Generated by Django 2.2.2 on 2019-06-29 20:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_auto_20190630_0114'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
