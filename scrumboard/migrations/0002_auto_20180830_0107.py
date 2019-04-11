# Generated by Django 2.1 on 2018-08-30 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scrumboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True)),
                ('story_points', models.IntegerField(blank=True, null=True)),
                ('business_value', models.IntegerField(blank=True, null=True)),
                ('list', models.ForeignKey(on_delete=True, related_name='cards', to='scrumboard.List')),
            ],
        ),
        migrations.DeleteModel(
            name='Cards',
        ),
    ]
