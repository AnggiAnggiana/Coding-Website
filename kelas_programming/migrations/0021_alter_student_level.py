# Generated by Django 5.0.1 on 2024-01-06 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kelas_programming', '0020_alter_profile_activation_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='level',
            field=models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Expert', 'Expert')], default='Beginner', max_length=30),
        ),
    ]
