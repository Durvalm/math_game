# Generated by Django 4.0.4 on 2022-05-20 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('math_game', '0003_remove_math_user_input'),
    ]

    operations = [
        migrations.AlterField(
            model_name='math',
            name='session_key',
            field=models.CharField(max_length=100),
        ),
    ]
