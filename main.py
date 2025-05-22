import time
from datetime import datetime, timedelta
from sheet_talker import SheetTalker
from retrievers import retrieve_cheapest_flight, retrieve_flight_list
from flight_searcher import FlightSearcher
from announcer import Announcer

ORIGIN_CITY_CODE = "LON"

sheet_talker = SheetTalker()
announcer = Announcer()
flight_searcher = FlightSearcher()
tomorrow = datetime.now() + timedelta(days=1)
six_months_from_today = datetime.now() + timedelta(days=(6 * 30))

def flight_list_helper(ze_destination, is_direct=True):
    return retrieve_flight_list(flight_searcher.check_new_flights(
        ORIGIN_CITY_CODE,
        ze_destination["iataCode"],
        from_time=tomorrow,
        to_time=six_months_from_today,
        is_direct=is_direct
    ))

for destination in sheet_talker.get_destinations():
    flight_list = flight_list_helper(destination)

    if flight_list is None:
        flight_list = flight_list_helper(destination, False)

    cheapest_flight = retrieve_cheapest_flight(flight_list)

    if float(cheapest_flight.price) < float(destination["lowestPrice"]):
        announcer.announce(
            destination["lowestPrice"],
            cheapest_flight.price,
            cheapest_flight.origin_airport,
            cheapest_flight.destination_airport,
            cheapest_flight.departure_date,
            cheapest_flight.return_date,
            cheapest_flight.number_of_stops
        )
    time.sleep(2)
