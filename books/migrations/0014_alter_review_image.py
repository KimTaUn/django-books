# Generated by Django 3.2.4 on 2021-08-15 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_alter_review_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='image',
            field=models.ImageField(null=True, upload_to='images/review'),
        ),
    ]