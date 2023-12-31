# Generated by Django 4.2.3 on 2023-07-21 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=20, null=True)),
                ('email', models.EmailField(blank=True, max_length=30, null=True)),
                ('image', models.ImageField(upload_to='profile_pic/')),
                ('age', models.PositiveBigIntegerField()),
                ('adress', models.TextField(max_length=200)),
                ('phone', models.CharField(max_length=15)),
                ('date_of_birth', models.DateField()),
                ('religion', models.CharField(blank=True, choices=[('Bouddho', 'four'), ('Christian', 'three'), ('Muslim', 'one'), ('Hindu', 'two'), ('others', 'five')], max_length=10, null=True)),
                ('gender', models.CharField(blank=True, choices=[('others', 'three'), ('Female', 'two'), ('Male', 'one')], max_length=8, null=True)),
            ],
        ),
    ]
