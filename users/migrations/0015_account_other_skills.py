# Generated by Django 3.2.20 on 2024-04-17 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_remove_account_other_skills'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='other_skills',
            field=models.TextField(blank=True, null=True, verbose_name='Other skills JSON'),
        ),
    ]