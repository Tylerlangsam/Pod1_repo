from Shawn_StationsChallenge import SubwayStation, BusStation

Sues_Rendezvous = BusStation('Sues Rendezvous', '96 Gramatan Ave', ['B22', 'B26', 'B99'])

Starlets = BusStation('Starlets', '49-09 25th Ave', ['Woodside', 'Corona', 'Jamaica'])

BadaBing = SubwayStation('BadaBing', '77 Jersey Road', ['6', '4', 'L'])

Sues_Rendezvous.show_info()
Sues_Rendezvous.close_station()
Sues_Rendezvous.show_info()

Starlets.show_info()
Starlets.close_station()
Starlets.show_info()

BadaBing.show_info()
