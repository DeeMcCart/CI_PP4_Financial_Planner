# Generated by Django 3.2.22 on 2023-11-12 08:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fp_personal', '0013_alter_useraction_parent_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserFavourite',
        ),
    ]
