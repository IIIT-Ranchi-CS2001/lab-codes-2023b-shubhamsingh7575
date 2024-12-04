import pandas as pd
import numpy as np

p=pd.read_csv('AQI_Data.csv')
print("First 8 row : ",p.head(8))
print("Last 5 row :",p.tail(5))




print(p.info())



# Question no. d) mean ,max,and min

mean_aqi_per_city = {city: np.mean(p['AQI'][p['City'] == city]) for city in np.unique(p['City'])}
max_PM_per_city= {city: np.max(p['PM2.5'][p['City'] == city]) for city in np.unique(p['City'])}
min_PM10_per_city={city: np.min(p['PM10'][p['City'] == city]) for city in np.unique(p['City'])}
print("Mean AQI per city: ",mean_aqi_per_city)
print("Max PM per city: ",max_PM_per_city)
print("Min PM10 per city: ",min_PM10_per_city)
