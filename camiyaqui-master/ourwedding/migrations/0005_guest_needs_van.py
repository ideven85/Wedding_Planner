# Generated by Django 2.2.4 on 2019-09-04 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ourwedding', '0004_profile_needs_van'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='needs_van',
            field=models.BooleanField(default=False, help_text='Do you need transport?', verbose_name='Van'),
        ),
    ]
