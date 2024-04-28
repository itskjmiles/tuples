def format_flight_itineraries(itineraries):
    formatted_itineraries = ""
    for i, itinerary in enumerate(itineraries, 1):
        traveler_name, origin, destination = itinerary
        formatted_itineraries += f"Itinerary {i}: {traveler_name} - From {origin} to {destination}\n"
    return formatted_itineraries

itineraries = itineraries = [
    ("Alice", "New York", "London"),
    ("Bob", "Tokyo", "San Francisco"),
    ("Charlie", "Paris", "Sydney"),
    ("David", "London", "Tokyo"),
    ("Emma", "Sydney", "New York")
]

result = format_flight_itineraries(itineraries)
print(result)
