from my_utils import get_column

#print the total number of files in a specified country
country='United States of America'
country_column = 0
fires_column = 3
file_name = 'Agrofood_co2_emission.csv'
fires = get_column(file_name,country_column,country,result_column = fires_column)

totalFires = 0

for fire in fires:
    totalFires += float(fire)
print(f'Total Fires in {country} between 1990 and 2020: {totalFires}')
# print(sum(int(fires)))
