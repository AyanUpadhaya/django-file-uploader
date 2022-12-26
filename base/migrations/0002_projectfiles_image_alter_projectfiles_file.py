# Generated by Django 4.1.4 on 2022-12-26 17:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectfiles',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectfiles',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
