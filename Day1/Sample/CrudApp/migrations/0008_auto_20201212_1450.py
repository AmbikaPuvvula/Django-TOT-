# Generated by Django 2.2.14 on 2020-12-12 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0007_emp'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
