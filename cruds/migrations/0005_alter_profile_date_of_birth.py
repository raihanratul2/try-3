# Generated by Django 4.2.3 on 2023-07-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cruds', '0004_alter_profile_gender_alter_profile_religion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(auto_now_add=True, verbose_name='Date'),
        ),
    ]
