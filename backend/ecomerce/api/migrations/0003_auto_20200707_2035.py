# Generated by Django 3.0.8 on 2020-07-08 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20200707_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaints',
            name='published',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicacion'),
        ),
    ]
