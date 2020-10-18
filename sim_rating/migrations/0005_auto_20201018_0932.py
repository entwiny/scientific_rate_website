# Generated by Django 3.0.8 on 2020-10-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sim_rating', '0004_auto_20201003_1611'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='display',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='source',
            name='source',
            field=models.CharField(help_text='Enter an article source ( e.g. The Times)', max_length=30),
        ),
    ]
