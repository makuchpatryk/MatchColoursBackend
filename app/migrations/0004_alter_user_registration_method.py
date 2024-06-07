# Generated by Django 4.2.13 on 2024-06-07 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='registration_method',
            field=models.CharField(choices=[('google', 'Google'), ('github', 'Github')], default='email', max_length=10),
        ),
    ]