# Generated by Django 2.2.1 on 2019-05-16 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('char_info', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='jp_release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='media',
            name='us_release_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]