# Generated by Django 4.0.2 on 2022-02-26 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_category_remove_food_source_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='source_name',
        ),
        migrations.RemoveField(
            model_name='category',
            name='source_url',
        ),
        migrations.AddField(
            model_name='food',
            name='source_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='food',
            name='source_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='food',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]