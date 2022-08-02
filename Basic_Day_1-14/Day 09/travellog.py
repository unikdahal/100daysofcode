
travel_log=[
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris","Lille","Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin","Hamburg","Stuttgart"]
    },
]
def add_new_country(name,nooftimes,city):
    travel_log.append(
        {
            "country": name,
            "visits": nooftimes,
            "cities": city
        },
    )
add_new_country("Russia",2,["Moscow","Saint Pearl"])
print(travel_log[2])
