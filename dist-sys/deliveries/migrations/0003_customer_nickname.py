# Generated by Django 2.1.1 on 2019-03-16 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deliveries', '0002_auto_20190316_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='nickname',
            field=models.CharField(default='joe', max_length=200),
            preserve_default=False,
        ),
    ]
