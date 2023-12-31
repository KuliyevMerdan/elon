# Generated by Django 4.2.3 on 2023-07-07 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elon', '0002_alter_feature_options_alter_menu_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='bottom_line',
            field=models.CharField(max_length=100, verbose_name='Нижняя строка'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='mid_line',
            field=models.CharField(max_length=100, verbose_name='Средняя строка'),
        ),
        migrations.AlterField(
            model_name='feature',
            name='top_line',
            field=models.CharField(max_length=100, verbose_name='Верхняя строка'),
        ),
    ]
