# Generated by Django 4.2.10 on 2024-02-14 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviewapp', '0003_alter_review_movie_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='movie_id',
            new_name='movie',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='user_id',
            new_name='user',
        ),
    ]