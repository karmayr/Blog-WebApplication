# Generated by Django 4.2.3 on 2023-07-11 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_blog_updated_at_alter_blog_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.SlugField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
