# Generated by Django 3.2.16 on 2022-11-15 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='lead_paragraph',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
