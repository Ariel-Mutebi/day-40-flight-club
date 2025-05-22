class Announcer:
        def announce(self, set_low_price, price, departure_airport, arrival_airport, outbound_date, inbound_date, number_of_stops):
                print(f"Flight deal for price lower than set low price of {set_low_price} found!")
                print(f"Price: {price}")
                print(f"Departure airport IATA code: {departure_airport}")
                print(f"Arrival airport IATA code: {arrival_airport}")
                print(f"Outbound date: {outbound_date}")
                print(f"Inbound date: {inbound_date}")
                if number_of_stops > 0:
                        print(f"Number of stop-overs: {number_of_stops}")