# ===== MIGRATION COMMANDS =====
# python manage.py makemigrations
# python manage.py sqlmigrate searches ___
# python manage.py migrate
# ===== MIGRATION COMMANDS =====


from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=30, unique=True, default="")

    avg_procedure_cost = models.IntegerField()
    avg_waiting_time   = models.IntegerField()
    quality_rank       = models.IntegerField()

    hospital_1 = models.CharField(max_length=30, unique=True, default="")
    hospital_2 = models.CharField(max_length=30, unique=True, default="")
    hospital_3 = models.CharField(max_length=30, unique=True, default="")