# Generated by Django 4.1.5 on 2023-04-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mini_amazon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_address', models.CharField(max_length=200)),
            ],
        ),
    ]
