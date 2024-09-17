# Generated by Django 4.2.16 on 2024-09-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdata',
            name='employee_id',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='salesdata',
            name='employee_name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
