# Generated by Django 4.1.1 on 2024-02-28 02:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_todocategory_name_alter_todopage_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todocategory',
            name='name',
            field=models.CharField(max_length=16),
        ),
    ]
