# Generated by Django 4.2.2 on 2023-07-16 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_alter_order_form_unique_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order_form',
            name='unique_key',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
