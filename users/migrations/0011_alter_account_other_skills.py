from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_account_other_skills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='other_skills',
            field=models.TextField(default='[]', null=True, verbose_name='Other skills'),
        ),
    ]
