# Generated by Django 2.1 on 2018-08-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0002_auto_20180830_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='list',
            field=models.ForeignKey(on_delete=False, related_name='cards', to='scrumboard.List'),
        ),
    ]
