# Generated by Django 2.2.14 on 2020-12-14 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0012_auto_20201214_1146'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='lang',
            field=models.CharField(choices=[('Telugu', 'Telugu'), ('Hindi', 'Hindi'), ('English', 'English')], max_length=10, null=True),
        ),
    ]