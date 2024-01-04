# Generated by Django 4.2.7 on 2023-12-16 14:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kelas_programming', '0013_student_kelasku'),
    ]

    operations = [
        migrations.CreateModel(
            name='PickClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kelas_siswa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kelas_programming.class')),
                ('siswa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kelas_programming.student')),
            ],
        ),
    ]
