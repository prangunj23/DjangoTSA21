# Generated by Django 3.2.8 on 2022-01-12 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('default', '0003_alter_event_difficulty'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='lichessusername',
            field=models.CharField(default=None, max_length=64),
            preserve_default=False,
        ),
    ]