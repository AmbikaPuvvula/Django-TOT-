# Generated by Django 3.0.6 on 2020-12-11 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CrudApp', '0006_auto_20201211_1742'),
    ]

    operations = [
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=50)),
                ('empid', models.CharField(max_length=20)),
                ('sal', models.IntegerField()),
                ('dept', models.CharField(max_length=20)),
            ],
        ),
    ]
