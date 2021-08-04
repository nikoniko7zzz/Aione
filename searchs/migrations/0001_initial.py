# Generated by Django 2.1.15 on 2021-07-22 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keyword1', models.CharField(max_length=128, verbose_name='キーワード1')),
                ('keyword2', models.CharField(max_length=128, verbose_name='キーワード2')),
                ('keyword3', models.CharField(max_length=128, verbose_name='キーワード3')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='作成日')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
            ],
        ),
    ]