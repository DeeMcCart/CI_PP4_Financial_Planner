# Generated by Django 3.2.22 on 2023-11-15 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fp_personal', '0014_delete_userfavourite'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraction',
            name='user_action_url',
            field=models.URLField(blank=True),
        ),
    ]
