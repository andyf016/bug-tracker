# Generated by Django 3.1 on 2020-08-28 03:51

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('time_stamp', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField()),
                ('status', models.CharField(choices=[('N', 'New'), ('IP', 'In Progress'), ('D', 'Done'), ('IN', 'Invalid')], default='N', max_length=20, null=True)),
            ],
        ),
    ]