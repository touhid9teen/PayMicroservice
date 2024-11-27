# Generated by Django 5.1.3 on 2024-11-27 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scheduler',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('user_number', models.CharField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_frequency', models.CharField()),
                ('narration', models.TextField()),
                ('service_name', models.TextField()),
                ('service_url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
