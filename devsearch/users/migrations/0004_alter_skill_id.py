# Generated by Django 3.2.7 on 2021-09-13 14:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210913_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
