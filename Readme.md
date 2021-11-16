# P3_Geospatial_Data

# Objetive

In this project we have to find a new location for our company.

Our company is related to gaming industry.

It has to be placed in Madrid, Spain.
We will use the data base Companies in MongoDB to find similar companies.
Our strategy will be to acquire our new location to one existing company listed in the Companies BD.

It should fit several conditions, such as:

    Design companies closer than 5 km,
	At least 3 different Schools in 5 km area,
	Close to tech startups that have raised at least 1 Million dollars,
	Starbucks not too far is mandatory,
    Good communications with airport, closer than 30 km,
    Some bars in 1 km around,
    A Vegan restaurante within 3 kms,
	A Basketball stadium must be around 10 Km,
    Dog-hairdresser closer than 5 km,

At first stage I will focus on fullfill only 5 conditions:
	
	- Starbucks
	- Bars
	- Schools
	- Basketball Stadium in the city
	- Airport

The api of Foursquare will be used to find services close to a given location.

# Deliverables

	- Readme,
	- 1 Notebook for selecting potential new locations
	- 1 Notebook for searching the available services close to the potential new locations
	- 1 CSV and 1 JSON files with the list of potential locations
	- Several JSON files with a list of services for each location
	- A .py file with several used functions
	- Some exported html files including interactive maps.
