# Vincenzo Mezzio ISI 300 Car Collision Rates Project

#loading our data
import pandas as pd
signal = pd.read_csv('DOT_Street_Lights_and_Traiffc_Signals.csv')
crash = pd.read_csv('Motor_Vehicle_Collisions_Crashes_2020.csv')
people = pd.read_csv('Motor_Vehicle_Collisions_People.csv')

#test 
print(crash)

#first five rows
print(crash.head())

#last 5
print(people.tail(5))

#info about df
print(crash.describe())

#show columns with crash date and borough name, first 10
print(crash[ ['CRASH DATE\xa0', 'BOROUGH\xa0'] ].head(10) )

#test
#print(sorted(crash))

#reference
#print("Show columns 'year' and 'team'")
#print( df_football[ ['year','team'] ].head() )

#
#print(crash[ crash['CRASH TIME\xa0'] == 11:00])

#reference 2 
#(df_football[ df_football['team'] == 'Packers' ] 