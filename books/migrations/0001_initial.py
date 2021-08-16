# Generated by Django 3.2.4 on 2021-08-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('pageCount', models.IntegerField()),
                ('thumbnailUrl', models.CharField(max_length=256)),
                ('shortDescription', models.CharField(max_length=256)),
                ('longDescription', models.TextField()),
            ],
        ),
    ]