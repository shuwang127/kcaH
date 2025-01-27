# Generated by Django 2.2.7 on 2020-03-28 12:20

from django.db import migrations, models
import place.models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', models.IntegerField(blank=True, null=True, verbose_name='Page')),
                ('title', models.CharField(blank=True, max_length=256, null=True, verbose_name='Title')),
                ('cover', models.ImageField(blank=True, null=True, upload_to=place.models.media_file_path, verbose_name='Cover')),
            ],
        ),
    ]
