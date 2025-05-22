class Flight:
    #Create object from flight data
    def __init__(self, price, origin_airport, destination_airport, departure_date, return_date, number_of_stops):
        self.price = price
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.departure_date = departure_date
        self.return_date = return_date
        self.number_of_stops = number_of_stops