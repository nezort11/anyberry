# Generated by Django 3.2.7 on 2021-09-02 10:51

from django.db import migrations
import djmoney.models.fields
import djmoney.models.validators


class Migration(migrations.Migration):

    dependencies = [
        ('berries', '0002_auto_20210902_1043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='berry',
            name='price',
            field=djmoney.models.fields.MoneyField(decimal_places=2, help_text='Enter price of 1 unit in RUB', max_digits=10, validators=[djmoney.models.validators.MinMoneyValidator(0)], verbose_name='Price'),
        ),
    ]
