# Generated by Django 2.2.2 on 2019-06-16 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='create_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]