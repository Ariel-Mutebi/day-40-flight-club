from flight import Flight

def retrieve_cheapest_flight(flight_list):
    first_flight = flight_list[0]
    origin = retrieve_origin(first_flight)
    number_of_stops = retrieve_number_of_stops(first_flight)
    destination = retrieve_destination(first_flight, number_of_stops)
    departure_date = retrieve_departure_date(first_flight)
    return_date = retrieve_return_date(first_flight)
    lowest_price = retrieve_price(first_flight)

    cheapest_flight = Flight(lowest_price, origin, destination, departure_date, return_date, number_of_stops)

    for flight in flight_list[1:]:
        price = retrieve_price(flight)
        if price < lowest_price:
            lowest_price = price
            origin = retrieve_origin(flight)
            number_of_stops = retrieve_number_of_stops(flight)
            destination = retrieve_destination(flight, number_of_stops)
            departure_date = retrieve_departure_date(flight)
            return_date = retrieve_return_date(flight)
            cheapest_flight = Flight(lowest_price, origin, destination, departure_date, return_date, number_of_stops)

    return cheapest_flight

def retrieve_flight_list(flight_json):
    if flight_json is None:
        return None
    flight_list = flight_json["data"]
    if not flight_list:
        return None
    return flight_list

def retrieve_price(flight):
    return float(flight["price"]["grandTotal"])

def retrieve_origin(flight):
    return flight["itineraries"][0]["segments"][0]["departure"]["iataCode"]

def retrieve_destination(flight, number_of_stops):
    return flight["itineraries"][0]["segments"][number_of_stops]["arrival"]["iataCode"]

def retrieve_departure_date(flight):
    return flight["itineraries"][0]["segments"][0]["departure"]["at"].split("T")[0]

def retrieve_return_date(flight):
    return flight["itineraries"][1]["segments"][0]["departure"]["at"].split("T")[0]

def retrieve_number_of_stops(flight):
    return len(flight["itineraries"][0]["segments"]) - 1
