# Generated by Django 3.1.7 on 2021-11-25 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20211123_1321'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
