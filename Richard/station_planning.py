from stations_challenge import Station
from stations_challenge import SubwayStation
from stations_challenge import BusStation

# Example Bus Station
station_name = 'Chicago'
location = 'Fullerton & Halsted'
lines = ['Green 12', 'Green 54', 'Red 80']

station_A = BusStation(station_name, location, lines)
station_A.show_info()
station_A.close_station()
station_A.show_info()

# Example Subway Station
station_name = 'New York'
location = '4th street and 8th Ave'
lines = ['Blue', 'Metro North', 'Path']

station_B = SubwayStation(station_name, location, lines)
station_B.show_info()

# Example Station
station_name = 'San Francisco'
location = 'Pacific Heights and Marina'
lines = ['BART', 'Train', 'Airport']

station_C = Station(station_name, location)
station_C.show_info()