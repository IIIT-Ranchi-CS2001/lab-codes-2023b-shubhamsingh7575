import numpy as np
import matplotlib.pyplot as plt

# Given COVID-19 data
covid_data = np.array([
    [1500, 2000, 1800, 1200, 900],  # Day 1
    [1600, 2100, 1900, 1300, 950],  # Day 2
    [1700, 2200, 2000, 1400, 1000], # Day 3
    [1650, 2150, 1950, 1350, 980],  # Day 4
    [1750, 2250, 2050, 1450, 1020], # Day 5
    [1800, 2300, 2100, 1500, 1050], # Day 6
    [1900, 2400, 2200, 1600, 1100], # Day 7
])

countries = ['Country_A', 'Country_B', 'Country_C', 'Country_D', 'Country_E']

# Basic Statistics
total_cases_per_country = np.sum(covid_data, axis=0)
country_with_highest_cases = countries[np.argmax(total_cases_per_country)]

# Daily Analysis
average_cases_per_day = np.mean(covid_data, axis=1)
day_with_highest_total_cases = np.argmax(np.sum(covid_data, axis=1)) + 1

# Trends
percentage_change = ((covid_data[-1] - covid_data[0]) / covid_data[0]) * 100
country_with_highest_percentage_increase = countries[np.argmax(percentage_change)]

# Data Transformation - Normalizing the data
normalized_data = (covid_data - np.min(covid_data, axis=0)) / (np.max(covid_data, axis=0) - np.min(covid_data, axis=0))

# Visualization
plt.figure(figsize=(10, 6))
for i, country in enumerate(countries):
    plt.plot(range(1, 8), covid_data[:, i], label=country)

# Highlight the day with the highest total cases
plt.axvline(x=day_with_highest_total_cases, color='r', linestyle='--', label=f'Highest Cases: Day {day_with_highest_total_cases}')
plt.xlabel('Day')
plt.ylabel('Number of Cases')
plt.title('Daily COVID-19 Cases for Each Country')
plt.legend()
plt.show()

# Output Results
print("Total cases reported in each country over 7 days:", total_cases_per_country)
print("Country with the highest total cases:", country_with_highest_cases)
print("Average number of cases per day across all countries:", average_cases_per_day)
print("Day with the highest total number of cases across all countries:", day_with_highest_total_cases)
print("Percentage increase or decrease from Day 1 to Day 7 for each country:", percentage_change)
print("Country with the highest percentage increase:", country_with_highest_percentage_increase)
print("Normalized dataset:\n", normalized_data)