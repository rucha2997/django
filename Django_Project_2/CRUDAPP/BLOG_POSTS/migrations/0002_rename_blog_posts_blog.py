# Generated by Django 3.2.6 on 2021-08-10 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('BLOG_POSTS', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='BLOG_POSTS',
            new_name='Blog',
        ),
    ]