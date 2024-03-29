# Generated by Django 4.2 on 2023-05-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("spravki", "0008_travel_choice_alter_bassein_choice"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bassein",
            name="choice",
            field=models.CharField(
                choices=[
                    ("bassein", "Бассейн"),
                    ("sport", "Спорт"),
                    ("sabeg", "Забег"),
                    ("sapliv", "Заплыв"),
                ],
                help_text="Выберети нужную справку для\n                   правильного отображения страницы",
                max_length=100,
                null=True,
                verbose_name="Выбор справки спорт",
            ),
        ),
    ]
