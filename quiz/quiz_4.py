# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by *** and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict


agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = str(min(years)),str(max(years))
# Insert your code here
with open(agricultural_land_filename,"r", encoding="utf-8") as af, open(forest_filename,"r", encoding="utf-8") as ff:
    for i in range(4):
        af.readline() #jump through the header
        ff.readline()
    csv_af = csv.DictReader(af)
    csv_ff = csv.DictReader(ff)
    country_dict = defaultdict(list)
    for country in csv_af:
        if country[year_1] != '' and country[year_2] != '':
            y1 = float(country[year_1])
            y2 = float(country[year_2])
            if y1 < y2:
                country_dict[country['Country Name']].append(y2 - y1)

    for country in csv_ff:
        if country[year_1] != '' and country[year_2] != '':
            y1 = float(country[year_1])
            y2 = float(country[year_2])
            if country['Country Name'] in country_dict:
                if y1 < y2:
                    country_dict[country['Country Name']].append(y2 - y1)
                else:
                    country_dict.pop(country['Country Name'])
        elif country['Country Name'] in country_dict:
            country_dict.pop(country['Country Name'])
    countries = [c[0]+f' ({c[1][0]/c[1][1]:.2f})' for c in sorted(country_dict.items(),key = lambda x: x[1][0] / x[1][1], reverse = True)[:top_n]]
print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))
    

