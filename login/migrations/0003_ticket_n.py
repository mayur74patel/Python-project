# Generated by Django 2.0.2 on 2018-04-10 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_ticket_d'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket_N',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_name', models.CharField(max_length=30)),
            ],
        ),
    ]
