# Generated by Django 4.2 on 2023-05-21 17:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sale", "0004_alter_sale_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="sale",
            name="choice",
            field=models.CharField(
                choices=[
                    ("services:ultrasound", "Узи"),
                    ("services:rentgen", "Рентген"),
                    ("services:analisi", "Анализы"),
                    ("services:fluromobil", "Флюромобиль"),
                ],
                help_text="Выберети нужную услугу для\n                   которой будет действовать акция",
                max_length=100,
                null=True,
                verbose_name="Выбор услуги",
            ),
        ),
    ]
