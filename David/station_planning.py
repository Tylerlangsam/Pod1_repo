from David_inheritance_challenge import Station
from David_inheritance_challenge import SubwayStation
from David_inheritance_challenge import BusStation

station_name = "Union Station"
location = "1 st and Mass Ave"
lines = ["Amtrak", "VRE"]

station_1 = Station(station_name, location)
station_1.show_info()

station_name = "Pentagon"
location = "Pentagon Building"
lines = ['Blue', 'Orange', 'Yellow']

station_2 = SubwayStation(station_name, location, lines)
station_2.show_info()

station_name = "Union Station"
location = "1 st and Mass Ave"
lines = ['NYC', 'Philadelphia', 'Richmond']

station_3 = BusStation(station_name, location, lines)
station_3.show_info




