# Generated by Django 5.0.6 on 2024-07-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_contato_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='contato',
            name='sobrenome',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
