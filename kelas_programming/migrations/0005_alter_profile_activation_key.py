# Generated by Django 4.2.7 on 2023-12-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kelas_programming', '0004_alter_profile_activation_key_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='activation_key',
            field=models.CharField(default=1, max_length=255, unique=True),
        ),
    ]