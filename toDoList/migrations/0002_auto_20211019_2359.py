# Generated by Django 3.2.8 on 2021-10-20 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoList', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='item_list',
        ),
        migrations.AddField(
            model_name='user',
            name='item_list',
            field=models.ManyToManyField(to='toDoList.ListItem'),
        ),
    ]
