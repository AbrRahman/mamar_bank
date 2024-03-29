# Generated by Django 5.0 on 2024-01-10 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transactions', '0002_transaction_bankrupt'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('bankrupt', models.BooleanField(default=False)),
            ],
        ),
        migrations.RemoveField(
            model_name='transaction',
            name='bankrupt',
        ),
    ]
