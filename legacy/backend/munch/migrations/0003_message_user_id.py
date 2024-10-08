# Generated by Django 4.2.15 on 2024-09-04 02:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('munch', '0002_alter_message_options_message_timestamp_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='user_id',
            field=models.CharField(default=django.utils.timezone.now, help_text='Unique identifier for the user.', max_length=100),
            preserve_default=False,
        ),
    ]
