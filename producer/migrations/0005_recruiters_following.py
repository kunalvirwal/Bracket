# Generated by Django 5.0 on 2023-12-29 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producer', '0004_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruiters',
            name='following',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
