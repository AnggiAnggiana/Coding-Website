# Generated by Django 4.2.7 on 2023-12-17 15:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kelas_programming', '0016_payment_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='name',
        ),
    ]
