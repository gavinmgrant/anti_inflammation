# Generated by Django 4.0.2 on 2022-02-26 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('source_name', models.CharField(max_length=100)),
                ('source_url', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='source_name',
        ),
        migrations.RemoveField(
            model_name='food',
            name='source_url',
        ),
        migrations.RemoveField(
            model_name='food',
            name='category',
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ManyToManyField(related_name='foods', to='list.Category'),
        ),
    ]
