# Generated by Django 4.2.2 on 2023-07-16 16:43

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_record_order_form'),
    ]

    operations = [
        migrations.AddField(
            model_name='order_form',
            name='udid',
            field=models.DurationField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='udid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
