# Generated by Django 2.2.2 on 2019-07-29 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0012_pdffiles_added_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pdffiles',
            name='added_by',
        ),
    ]