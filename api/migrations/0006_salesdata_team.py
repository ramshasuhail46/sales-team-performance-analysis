# Generated by Django 4.2.16 on 2024-09-18 00:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_remove_salesdata_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesdata',
            name='team',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sales_data', to='api.team'),
        ),
    ]
