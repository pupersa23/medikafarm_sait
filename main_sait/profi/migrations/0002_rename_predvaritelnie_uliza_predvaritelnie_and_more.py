# Generated by Django 4.2 on 2023-05-10 18:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("profi", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Predvaritelnie_Uliza",
            new_name="Predvaritelnie",
        ),
        migrations.DeleteModel(
            name="Predvaritelnie_Company",
        ),
        migrations.AlterModelOptions(
            name="predvaritelnie",
            options={
                "verbose_name": "Предварительный осмотр",
                "verbose_name_plural": "Предварительный осмотр",
            },
        ),
    ]
