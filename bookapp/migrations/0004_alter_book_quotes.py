# Generated by Django 4.2.7 on 2024-03-25 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_remove_genre_image_customuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='quotes',
            field=models.ManyToManyField(blank=True, to='bookapp.quote'),
        ),
    ]
