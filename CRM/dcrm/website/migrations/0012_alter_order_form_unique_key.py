# Generated by Django 4.2.2 on 2023-07-16 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_record_unique_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_form',
            name='unique_key',
            field=models.CharField(blank=True, default=1, editable=False, max_length=100),
            preserve_default=False,
        ),
    ]
