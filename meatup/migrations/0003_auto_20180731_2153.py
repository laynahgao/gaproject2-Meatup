# Generated by Django 2.0.5 on 2018-07-31 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meatup', '0002_user_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='user/%Y/%m/%d/'),
        ),
    ]
