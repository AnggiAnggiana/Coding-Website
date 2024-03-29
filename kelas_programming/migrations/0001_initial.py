# Generated by Django 4.2.7 on 2023-12-02 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Kelas')),
                ('language', models.CharField(max_length=120, verbose_name='language')),
                ('framework', models.CharField(max_length=120, verbose_name='Framework')),
                ('function', models.CharField(max_length=120, verbose_name='Function')),
                ('link', models.URLField(verbose_name='Link')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=60)),
                ('last_name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120, verbose_name='Programming Course')),
                ('date', models.DateTimeField(verbose_name='Course Date')),
                ('lecture', models.CharField(max_length=120, verbose_name='Lecturer')),
                ('description', models.TextField(blank=True)),
                ('kelas', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='kelas_programming.class')),
                ('myclass', models.ManyToManyField(blank=True, null=True, to='kelas_programming.student')),
            ],
        ),
    ]
