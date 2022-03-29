from stations_challenge import Station
from stations_challenge import SubwayStation
from stations_challenge import BusStation

# Example Bus Station
station_name = 'Los Angeles'
location = 'Union'
lines = ['Red 1', 'Pink 33', 'Blue 10']

station_A = BusStation(station_name, location, lines)
station_A.show_info()
station_A.close_station()
station_A.show_info()

# Example Subway Station
station_name = 'New York'
location = 'Times Square'
lines = ['Yellow', 'Brooklyn', 'inner city']

station_B = SubwayStation(station_name, location, lines)
station_B.show_info()

# Example Station
station_name = 'Port of Seattle'
location = 'Alaskin Way and Clay'
lines = ['Ferry', 'Bartts', 'Frieghts']

station_C = Station(station_name, location)
station_C.show_info() 