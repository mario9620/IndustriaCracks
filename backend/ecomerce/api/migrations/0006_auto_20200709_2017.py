# Generated by Django 3.0.8 on 2020-07-10 02:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_log_action'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='followers',
            unique_together={('follower_id', 'followed_id')},
        ),
    ]
