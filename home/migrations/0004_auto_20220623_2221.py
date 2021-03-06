# Generated by Django 3.2.7 on 2022-06-23 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_posts_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='Hasibul Islam', max_length=264),
        ),
        migrations.AlterField(
            model_name='post',
            name='img2',
            field=models.ImageField(blank=True, upload_to='static/uploads'),
        ),
        migrations.AlterField(
            model_name='post',
            name='img3',
            field=models.ImageField(blank=True, upload_to='static/uploads'),
        ),
    ]
