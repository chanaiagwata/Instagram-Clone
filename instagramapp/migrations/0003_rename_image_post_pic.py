# Generated by Django 3.2.10 on 2022-06-07 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instagramapp', '0002_followers_delete_tags_remove_comment_datetime_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='pic',
        ),
    ]
