# Generated by Django 3.0.7 on 2020-06-13 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_followerrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='nick_name',
            field=models.CharField(default='없음', max_length=32),
        ),
    ]