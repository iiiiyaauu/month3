# Generated by Django 3.2.9 on 2021-11-30 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(blank=True, null=True, upload_to='post_pic/')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('likes', models.IntegerField(default=0)),
                ('reposts', models.IntegerField(default=0)),
            ],
        ),
    ]
