# Generated by Django 2.1.3 on 2018-11-04 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tableapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='fromTime',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='activity',
            name='toTime',
            field=models.TimeField(null=True),
        ),
    ]