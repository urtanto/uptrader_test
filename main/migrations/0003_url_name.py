# Generated by Django 5.0.2 on 2024-02-12 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_menu_url_delete_childurl_delete_rooturl'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='name',
            field=models.CharField(default='test', max_length=255),
        ),
    ]
