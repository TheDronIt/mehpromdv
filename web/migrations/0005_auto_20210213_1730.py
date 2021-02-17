# Generated by Django 3.1.6 on 2021-02-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20210210_1708'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='kind',
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.PositiveSmallIntegerField(choices=[(11, 'Судовой'), (12, 'Пирсовый'), (13, 'Съемный портальный'), (14, 'Балки грузовые'), (15, 'Грузовой специальный'), (16, 'Грузовой арктический'), (21, 'Грузовой - перем. ток | мал. ср.'), (22, 'Грузовой - перем. ток | бол.'), (23, 'Пром. Грузовой - эл. привод | мал.'), (24, 'Пром. Грузовой - перем. ток | бол.'), (25, 'Вьюшка топенантная - перем. ток'), (26, 'Подъемно тяговая - перем. ток'), (27, 'Грузовой - перем. ток'), (28, 'Гидрологический'), (29, 'Пром. Лебедка или комплекс'), (210, 'Буксирная автом. эл. привод'), (211, 'Буксирно-технологическая эл. привод'), (212, 'Шлюпочная - гидр. привод'), (217, 'Трелевочная'), (218, 'Люктового закрытия - перем. ток'), (219, 'Траповая - перем. ток'), (31, 'Водоструйный стационарный'), (32, 'Водоструйный переносной')], verbose_name='category'),
        ),
    ]