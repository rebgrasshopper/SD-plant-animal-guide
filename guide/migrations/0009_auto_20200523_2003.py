# Generated by Django 2.2.12 on 2020-05-24 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0008_auto_20200523_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='other_uses',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
