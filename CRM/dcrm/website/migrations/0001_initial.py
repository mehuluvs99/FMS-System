# Generated by Django 4.2.2 on 2023-07-13 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('company_name', models.CharField(max_length=100)),
                ('mobile_no', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=20)),
                ('step_name_one', models.CharField(blank=True, max_length=100, null=True)),
                ('planned_date_one', models.DateTimeField(blank=True, null=True)),
                ('actual_date_one', models.DateTimeField(blank=True, null=True)),
                ('status_one', models.BooleanField(default=False)),
                ('timedelay_one', models.DurationField(blank=True, null=True)),
                ('step_name_two', models.CharField(blank=True, max_length=100, null=True)),
                ('planned_date_two', models.DateTimeField(blank=True, null=True)),
                ('actual_date_two', models.DateTimeField(blank=True, null=True)),
                ('status_two', models.BooleanField(default=False)),
                ('timedelay_two', models.DurationField(blank=True, null=True)),
            ],
        ),
    ]
