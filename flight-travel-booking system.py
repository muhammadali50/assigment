def find_top_3_cheapest_flights(preferred_airlines, budget, flights):
    affordable_flights = []
    for flight in flights:
        if flight["price"] <= budget and (not preferred_airlines or flight["airline"] in preferred_airlines):
            affordable_flights.append(flight)

    sorted_flights = sorted(affordable_flights, key=lambda x: x["price"])

    print("Top 3 Cheapest Flight Options:")
    for i, flight in enumerate(sorted_flights[:3], start=1):
        print(f"{i}. Airline: {flight['airline']}, Price: ${flight['price']}, Dates: {flight['dates']}")

preferred_airlines = ["Garuda Indonesia", "Singapore Airlines"]

flights = [
    {"airline": "Garuda Indonesia", "price": 1500, "dates": ["2024-07-01", "2024-07-15"]},
    {"airline": "Singapore Airlines", "price": 1700, "dates": ["2024-07-03", "2024-07-17"]},
    {"airline": "AirAsia", "price": 1200, "dates": ["2024-07-02", "2024-07-16"]},
    {"airline": "Lion Air", "price": 1800, "dates": ["2024-07-04", "2024-07-18"]}
]

find_top_3_cheapest_flights(preferred_airlines, 2000, flights)