# Generated by Django 4.0.5 on 2022-07-08 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_member_jumin_member_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='id',
        ),
        migrations.AlterField(
            model_name='member',
            name='userid',
            field=models.CharField(max_length=18, primary_key=True, serialize=False),
        ),
    ]