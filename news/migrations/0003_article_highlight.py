# Generated by Django 2.2.24 on 2023-07-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20170711_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='highlight',
            field=models.BooleanField(default=False),
        ),
    ]