# Generated by Django 4.1.3 on 2022-11-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.IntegerField(max_length=11),
        ),
    ]