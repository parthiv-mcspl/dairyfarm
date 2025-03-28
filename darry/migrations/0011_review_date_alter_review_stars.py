# Generated by Django 5.0.7 on 2025-03-20 07:57

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('darry', '0010_remove_review_date_posted_remove_review_rating_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=3),
        ),
    ]
