# Generated by Django 4.1.5 on 2023-03-02 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("itapp", "0007_solvedcomplaints_rating_solvedcomplaints_suggestions"),
    ]

    operations = [
        migrations.AddField(
            model_name="complaints",
            name="ack",
            field=models.CharField(blank=True, max_length=100),
        ),
    ]