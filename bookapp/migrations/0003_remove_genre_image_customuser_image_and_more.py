# Generated by Django 4.2.7 on 2024-03-25 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0002_genre_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='image',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='default/account.png', upload_to='users'),
        ),
        migrations.AlterField(
            model_name='author',
            name='image',
            field=models.ImageField(null=True, upload_to='authors/'),
        ),
    ]
