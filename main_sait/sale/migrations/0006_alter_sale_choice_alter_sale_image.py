# Generated by Django 4.2 on 2023-05-22 16:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sale", "0005_alter_sale_choice"),
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
                    ("profi:predvaritelnie", "Предварительные"),
                    ("profi:pereodicheskiy", "Периодические"),
                    ("profi:vneocherednoy", "Внеочередной"),
                    ("profi:psihiatricheskoe", "Психиатрическое"),
                    ("profi:predsmenniy", "Предрейсы"),
                    ("spravki:gibdd", "Гаи"),
                    ("spravki:gims", "Гимс"),
                    ("spravki:gsy", "ГСу"),
                    ("spravki:gstayna", "Гостайна"),
                    ("spravki:spravki_086", "086у"),
                    ("spravki:student_095", "095у"),
                    ("spravki:spravki_sport", "Спорт"),
                    ("spravki:spravki_travel", "Путешествия"),
                    ("spravki:bolnichnij", "Больничный лист"),
                    ("knigki:medknizhki", "Книжки"),
                ],
                help_text="Выберети нужную услугу для\n                   которой будет действовать акция",
                max_length=100,
                null=True,
                verbose_name="Выбор услуги",
            ),
        ),
        migrations.AlterField(
            model_name="sale",
            name="image",
            field=models.ImageField(
                blank=True, upload_to="sale/", verbose_name="Картинка"
            ),
        ),
    ]
