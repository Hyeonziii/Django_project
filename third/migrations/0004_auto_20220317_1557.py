# Generated by Django 3.2.12 on 2022-03-17 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('third', '0003_rename_restaurant_review_restaurant'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='image',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='restaurant',
            name='password',
            field=models.CharField(default=None, max_length=20, null=True),
        ),
    ]
