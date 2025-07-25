# Generated by Django 5.2.3 on 2025-07-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]
