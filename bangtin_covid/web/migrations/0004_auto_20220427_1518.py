# Generated by Django 2.2 on 2022-04-27 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_covid_news'),
    ]

    operations = [
        migrations.AddField(
            model_name='covid_news',
            name='summarize_content',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='covid_news',
            name='content',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='covid_news',
            name='description',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='covid_news',
            name='img',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='covid_news',
            name='keywords',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='covid_news',
            name='public_date',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='covid_news',
            name='title',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='covid_news',
            name='url',
            field=models.CharField(max_length=5000),
        ),
    ]
