# run `python manage.py shell` and paste below code

from searches.models import Country
import random

countries = ['Australia', 'Canada', 'France', 'United Kingdom', 'United States of America']

uniq_ctr = 123
Country.objects.all().delete()
for country_name in countries:
	Country.objects.create(name=country_name, 
						   avg_procedure_cost=random.randint(10000,100000), 
						   avg_waiting_time=random.randint(30, 200),
						   quality_rank=random.randint(1, len(countries)),
						   hospital_1='Cool first' + str(uniq_ctr),
						   hospital_2='Cooler second' + str(uniq_ctr),
						   hospital_3='Coolset third' + str(uniq_ctr))
	uniq_ctr += 1
	