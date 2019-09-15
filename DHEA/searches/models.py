# ===== MIGRATION COMMANDS =====
# python manage.py makemigrations
# python manage.py sqlmigrate searches ___
# python manage.py migrate
# ===== MIGRATION COMMANDS =====


from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True, default="")
    city = models.CharField(max_length=30, unique=True, default="")

    avg_per_night_cost = models.IntegerField()
    quality_rank       = models.IntegerField()

    hospital_1_name = models.CharField(max_length=30, unique=True, default="")
    hospital_2_name = models.CharField(max_length=30, unique=True, default="")
    hospital_3_name = models.CharField(max_length=30, unique=True, default="")

    hospital_1_link = models.CharField(max_length=100, unique=True, default="")
    hospital_2_link = models.CharField(max_length=100, unique=True, default="")
    hospital_3_link = models.CharField(max_length=100, unique=True, default="")


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True, default="")
    city = models.CharField(max_length=30, unique=True, default="")

    avg_per_night_cost = models.IntegerField()
    quality_rank       = models.IntegerField()

    hospital_1_name = models.CharField(max_length=30, unique=True, default="")
    hospital_2_name = models.CharField(max_length=30, unique=True, default="")
    hospital_3_name = models.CharField(max_length=30, unique=True, default="")

    hospital_1_link = models.CharField(max_length=100, unique=True, default="")
    hospital_2_link = models.CharField(max_length=100, unique=True, default="")
    hospital_3_link = models.CharField(max_length=100, unique=True, default="")