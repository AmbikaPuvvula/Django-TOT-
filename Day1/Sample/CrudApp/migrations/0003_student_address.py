# Generated by Django 3.0.6 on 2020-12-11 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0002_employee'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(null=True),
        ),
    ]
