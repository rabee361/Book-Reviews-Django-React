# Generated by Django 4.2.7 on 2023-12-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0005_alter_author_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='about',
            field=models.TextField(default='test'),
        ),
    ]
