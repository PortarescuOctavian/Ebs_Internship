# Generated by Django 3.2.7 on 2021-09-18 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produse', '0002_auto_20210918_0939'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'verbose_name': 'Imagine'},
        ),
        migrations.RemoveField(
            model_name='image',
            name='url',
        ),
        migrations.RemoveField(
            model_name='product',
            name='photo',
        ),
        migrations.AddField(
            model_name='image',
            name='photo',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]