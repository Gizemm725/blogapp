# Generated by Django 5.2.3 on 2025-07-08 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_blog_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='Category',
        ),
        migrations.AddField(
            model_name='blog',
            name='categories',
            field=models.ManyToManyField(to='blog.category'),
        ),
    ]
