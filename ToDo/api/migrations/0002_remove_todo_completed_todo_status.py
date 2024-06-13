# Generated by Django 4.1.1 on 2024-02-26 02:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todo',
            name='completed',
        ),
        migrations.AddField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('UNFINISHED', 'Unfinished'), ('ACTIVE', 'Active'), ('FINISHED', 'Finished')], default='UNFINISHED', max_length=10),
        ),
    ]