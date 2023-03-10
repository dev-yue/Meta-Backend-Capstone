# Generated by Django 4.1.7 on 2023-02-23 00:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Name", models.IntegerField(max_length=11)),
                ("No_of_guests", models.CharField(max_length=255)),
                ("BookingDate", models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name="Menu",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Title", models.CharField(max_length=255)),
                ("Price", models.DecimalField(decimal_places=2, max_digits=10)),
                ("Inventory", models.IntegerField(max_length=5)),
            ],
        ),
    ]
