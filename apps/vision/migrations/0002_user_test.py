# Generated by Django 4.1.1 on 2022-09-14 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vision', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='test',
            field=models.BooleanField(default=False),
        ),
    ]