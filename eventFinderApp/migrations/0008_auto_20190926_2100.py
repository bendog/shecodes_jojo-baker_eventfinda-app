# Generated by Django 2.2 on 2019-09-26 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventFinderApp', '0007_auto_20190926_2059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_description',
            field=models.TextField(max_length=600),
        ),
    ]
