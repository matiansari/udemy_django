# Generated by Django 2.1.5 on 2019-02-18 22:38

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete='DO_NOTHING', related_name='comments', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete='DO_NOTHING', to=settings.AUTH_USER_MODEL),
        ),
    ]
