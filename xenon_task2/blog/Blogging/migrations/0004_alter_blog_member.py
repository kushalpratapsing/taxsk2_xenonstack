# Generated by Django 4.1.7 on 2023-09-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogging', '0003_rename_desc_blog_concern_rename_fname_blog_firstname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='member',
            field=models.CharField(max_length=10, null='off'),
        ),
    ]
