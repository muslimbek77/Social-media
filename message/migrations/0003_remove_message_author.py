# Generated by Django 4.0.6 on 2022-07-21 12:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_remove_message_post_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='author',
        ),
    ]