# Generated by Django 5.1.1 on 2024-09-28 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
