# Generated by Django 3.2.5 on 2021-08-12 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_merge_0003_auto_20210812_1540_0006_comment_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='publishYear',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='rate',
        ),
        migrations.AddField(
            model_name='book',
            name='book_size',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='book',
            name='publishedYear',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='pages',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='book',
            name='summary',
            field=models.TextField(blank=True, max_length=250),
        ),
    ]