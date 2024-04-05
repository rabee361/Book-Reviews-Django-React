# Generated by Django 4.2.7 on 2024-04-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_quote_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='currently_reading',
            field=models.ManyToManyField(related_name='currently_users', to='bookapp.book'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='read',
            field=models.ManyToManyField(related_name='read_users', to='bookapp.book'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='want_to_read',
            field=models.ManyToManyField(related_name='want_to_read_users', to='bookapp.book'),
        ),
        migrations.DeleteModel(
            name='ReadingList',
        ),
    ]
