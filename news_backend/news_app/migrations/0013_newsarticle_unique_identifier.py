# Generated by Django 5.0.3 on 2024-03-20 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0012_alter_newsarticle_url_to_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='unique_identifier',
            field=models.CharField(default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]
