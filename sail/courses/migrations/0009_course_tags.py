# Generated by Django 3.0.6 on 2020-05-31 04:42

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('courses', '0008_auto_20200528_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
