# Generated by Django 2.2.14 on 2020-12-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsApp', '0007_remove_register_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], max_length=10, null=True),
        ),
    ]
