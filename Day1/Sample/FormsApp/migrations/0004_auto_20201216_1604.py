# Generated by Django 2.2.14 on 2020-12-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FormsApp', '0003_register_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='gender',
            field=models.CharField(choices=[('Female', 'Female'), ('Male', 'Male'), ('Others', 'Others')], default='Male', max_length=10, null=True),
        ),
    ]
