# Generated by Django 2.2.2 on 2019-07-13 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfis', '0008_auto_20190708_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='cor',
            field=models.CharField(default='#455A64', max_length=10),
        ),
    ]
