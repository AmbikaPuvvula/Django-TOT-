# Generated by Django 2.2.14 on 2020-12-14 08:04

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0015_auto_20201214_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='lang',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Telugu', 'Telugu'), ('Hindi', 'Hindi'), ('English', 'English')], max_length=20, null=True),
        ),
    ]
