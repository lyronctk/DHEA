# ===== MIGRATION COMMANDS =====
# python manage.py makemigrations
# python manage.py sqlmigrate searches ___
# python manage.py migrate
# ===== MIGRATION COMMANDS =====


from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True, default="")
    city = models.CharField(max_length=30, unique=True, default="")

    avg_per_night_cost = models.IntegerField(default=0)
    quality_rank       = models.IntegerField(default=0)

    hospital_1_name = models.CharField(max_length=30, unique=True, default="")
    hospital_2_name = models.CharField(max_length=30, unique=True, default="")
    hospital_3_name = models.CharField(max_length=30, unique=True, default="")

    hospital_1_link = models.CharField(max_length=100, unique=True, default="")
    hospital_2_link = models.CharField(max_length=100, unique=True, default="")
    hospital_3_link = models.CharField(max_length=100, unique=True, default="")



class Procedure(models.Model):
    name    = models.CharField(max_length=30, default="")
    country = models.ForeignKey(Country, related_name='procedures', on_delete=models.PROTECT)

    avg_procedure_cost = models.IntegerField(default=0)
    avg_waiting_time   = models.IntegerField(default=0)
    avg_recovery_time  = models.IntegerField(default=0)

