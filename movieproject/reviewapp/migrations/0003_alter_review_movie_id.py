# Generated by Django 4.2.10 on 2024-02-14 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movieapp', '0004_movie_user'),
        ('reviewapp', '0002_rename_movie_review_movie_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='movie_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movieapp.movie'),
        ),
    ]
