# Generated by Django 5.0.3 on 2024-03-18 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('url', models.URLField()),
                ('image', models.ImageField(blank=True, upload_to='image/')),
            ],
        ),
    ]
