# Generated by Django 4.2.16 on 2024-11-05 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avtorizate', '0002_remove_user_phone_number_user_is_email_verified_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Card',
        ),
    ]