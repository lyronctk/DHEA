# run `python manage.py shell` and paste below code

from searches.models import Procedure
from searches.models import Country
import csv

Procedure.objects.all().delete()
Country.objects.all().delete()
with open('DHEA/CSVs/country_db.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	Country.objects.create(name=row['name'],
    						   city=row['city'],
    						   avg_per_night_cost=row['avg_per_night_cost'],
    						   quality_rank=row['quality_rank'],
    						   hospital_1_name=row['hospital_1_name'],
    						   hospital_2_name=row['hospital_2_name'],
    						   hospital_3_name=row['hospital_3_name'],
    						   hospital_1_link=row['hospital_1_link'],
    						   hospital_2_link=row['hospital_2_link'],
    						   hospital_3_link=row['hospital_3_link']
    						   )


with open('DHEA/CSVs/procedure_db.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
    	Procedure.objects.create(name=row['name'],
    						     country=Country.objects.get(name=row['country']),
    						     avg_procedure_cost=row['avg_procedure_cost'],
    						     avg_waiting_time=row['avg_waiting_time'],
    						     avg_recovery_time=row['avg_recovery_time']
    						    )





