# Generated by Django 3.2.16 on 2023-03-07 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_forum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='forum',
            name='answer',
            field=models.TextField(default=True, max_length=500),
        ),
    ]
