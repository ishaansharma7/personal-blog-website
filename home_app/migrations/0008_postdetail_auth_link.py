# Generated by Django 3.1.5 on 2021-01-27 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0007_auto_20210127_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdetail',
            name='auth_link',
            field=models.URLField(null=True),
        ),
    ]
