# Generated by Django 3.1.7 on 2021-03-16 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0002_profile_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='username',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='email',
        ),
        migrations.AddField(
            model_name='profile',
            name='fav_coin',
            field=models.TextField(default='BTC', max_length=4),
        ),
    ]
