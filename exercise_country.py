
countries = [
    {"name": "China", "population": 1425178782},
    {"name": "India", "population": 1441719852},
    {"name": "United States", "population": 3346831284},
    {"name": "France", "population": 66352000},
    {"name": "Nepal", "population": 1577361}
]

biggest_country = countries[0]
for country in countries:
    print(f"Country: {country['name']}, Population: {country['population']}")
    if country["population"] > biggest_country["population"]:
        biggest_country = country


print(f"The biggest country is {biggest_country["name"]} with a population of {biggest_country["population"]:}")

        











