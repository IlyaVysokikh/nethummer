# Generated by Django 4.2.6 on 2023-11-15 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_textcontent_text'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagecontent',
            name='text_content',
        ),
        migrations.RemoveField(
            model_name='videocontent',
            name='text_content',
        ),
    ]
