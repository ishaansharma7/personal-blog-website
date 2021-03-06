# Generated by Django 3.1.5 on 2021-01-27 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_title', models.CharField(max_length=256)),
                ('post_id', models.PositiveIntegerField()),
                ('github_link', models.URLField(blank=True, null=True)),
                ('post_desc', models.TextField()),
                ('creation_date', models.DateField()),
                ('post_video', models.URLField(blank=True, null=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
    ]
