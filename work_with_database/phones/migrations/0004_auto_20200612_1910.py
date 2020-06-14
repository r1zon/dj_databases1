# Generated by Django 2.2.10 on 2020-06-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0003_auto_20200612_1839'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='image',
            field=models.ImageField(default='none', upload_to=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='phone',
            name='lte_exists',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
