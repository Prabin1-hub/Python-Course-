countries = ["Nepal", "France",  "USA"]
print("second country", countries[1])
countries.append("Germany")
remove_country = countries.pop(0)
for country in countries:
    print(country)