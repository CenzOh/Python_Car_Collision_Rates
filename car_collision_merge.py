# ISI 300   Vincenzo Mezzio     Car Collision Rates Merge

#loading our data
import pandas as pd

crash = pd.read_csv('Motor_Vehicle_Collisions_Crashes_2020.csv')
weather = pd.read_csv('weather_nyc_4-1-21_4-8-21.csv')

print(crash)

#first five rows
print(crash.head())

#last 5
print(crash.tail(5))

#info about df
print(crash.describe())

#show columns with crash date and borough name, first 10
print(crash[ ['Date', 'BOROUGH '] ].head(10) )


crash_4_2 = crash[ crash['Date'].str.contains("4/3/2021")] # filters for only 2020 data

print(crash_4_2)
print()

#print(pd.merge(crash,people,on='CRASH DATE\xa0'))
#print( from_csv[ from_csv['team'] == 'Packers' ] )
#print(pd.merge(left,right,on='subject'))


print(weather)
print()
#print(weather[ weather['CRASH DATE\xa0'].str.contains("4/3/2021")]) # prints out weather for 4/3/2021

merged = pd.merge(crash,weather,on='Timestamp') # merge
print('Merged')
print(merged)
print()



#print(df_football['year'] == 2012) #example of filter

#Merge will work correctly if each row has a unique aspect (can't all just be 4/3/2021, for instance)

#analyze collisions vs weather patterns. Printing seperately to see them on Spyder terminal
print(merged[['Timestamp', 'CONTRIBUTING FACTOR VEHICLE 1 ', 'Wind Speed [10 m] km/h']]) #wind speed
#Distraction (4)
#Too Close (5)
#Most of these accidents occurred with high winds.
print()
print(merged[['Timestamp', 'CONTRIBUTING FACTOR VEHICLE 1 ', 'Temperature']]) #temperature
#20-29: 3 accidents
#30-39: 16 accidents
#40-49: 3 accidents
#50+: 2 accidents
#Accidents peak in 30-39 degree range
print()
print(merged[['Timestamp', 'CONTRIBUTING FACTOR VEHICLE 1 ', 'Relative Humidity [2 m] %']]) #humidity
#20-29: 5 accidents
#30-39: 6 accidents
#40-49: 9 accidents
#50-59: 2 accidents
#60+: 2 accidents
#Interestingly, as the humidity increases, more accidents occur. Not really true for 50+


#Charting
import matplotlib.pyplot as plt # library to draw charts 
import numpy as np

#Groupby only works on the attribute that joined the tables.

merged.groupby(['Timestamp']).agg({'Wind Speed [10 m] km/h': [np.mean]}).plot(kind='bar') #displaying avg wind speeds in bar graph based on dates and times
#merged.groupby(['Timestamp']).agg({'Wind Speed [10 m] km/h': [np.mean]}).plot(kind='kde')
merged.groupby(['Timestamp', 'CONTRIBUTING FACTOR VEHICLE 1 ']).agg({'Wind Speed [10 m] km/h': [np.mean]}).plot(kind='kde')
#Most accidents occured with high wind speeds

merged.groupby(['Timestamp']).agg({'Temperature': [np.mean]}).plot(kind='hist') #temperature in bar graph, average
merged.groupby(['Timestamp', 'CONTRIBUTING FACTOR VEHICLE 1 ']).agg({'Temperature': [np.mean]}).plot(kind='kde') 
#most accidents occurred with temperature between 30-40

merged.groupby(['Timestamp']).agg({'Relative Humidity [2 m] %': [np.mean]}).plot(kind='hist') #histogram displaying humidity average
merged.groupby(['Timestamp', 'CONTRIBUTING FACTOR VEHICLE 1 ']).agg({'Relative Humidity [2 m] %': [np.mean]}).plot(kind='kde') 
#most accidents occurred with humidity around 40-50%

#Weather does seem to affect car accidents!