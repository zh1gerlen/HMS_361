# Generated by Django 3.0.7 on 2022-11-30 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20221201_0441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='bloodgroup',
        ),
        migrations.AddField(
            model_name='patient',
            name='caregiver',
            field=models.CharField(default=880055535, max_length=10, verbose_name='88005553535'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='government_id',
            field=models.CharField(default=1, max_length=10, verbose_name='1'),
            preserve_default=False,
        ),
    ]