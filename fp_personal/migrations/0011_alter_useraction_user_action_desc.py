# Generated by Django 3.2.22 on 2023-11-11 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fp_blog', '0006_comment_user'),
        ('fp_personal', '0010_alter_useraction_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraction',
            name='user_action_desc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_actions', to='fp_blog.action'),
        ),
    ]