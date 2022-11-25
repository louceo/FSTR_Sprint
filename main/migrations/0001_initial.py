# Generated by Django 4.1.3 on 2022-11-25 09:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='coordinates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.ImageField(upload_to=None)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='level_diff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=10)),
                ('difficulty', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('fam', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('otc', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='pereval_added',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beautyTitle', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50, unique=True)),
                ('other_titles', models.CharField(max_length=50)),
                ('connect', models.TextField(max_length=255)),
                ('status', models.CharField(choices=[('new', 'new'), ('pending', 'pending'), ('accepted', 'accepted'), ('rejected', 'rejected')], default=('new', 'new'), max_length=10)),
                ('coords', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.coordinates')),
                ('images', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.img')),
                ('level', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.level_diff')),
            ],
        ),
    ]
