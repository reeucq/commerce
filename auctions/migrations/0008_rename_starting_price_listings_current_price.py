# Generated by Django 3.2.3 on 2021-05-30 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_listings_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listings',
            old_name='starting_price',
            new_name='current_price',
        ),
    ]