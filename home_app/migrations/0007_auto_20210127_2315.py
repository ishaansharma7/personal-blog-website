# Generated by Django 3.1.5 on 2021-01-27 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0006_auto_20210127_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdetail',
            name='post_video',
            field=models.URLField(blank=True, null=True),
        ),
    ]