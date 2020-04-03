import pandas as pd
ftrips = pd.read_csv("trips.txt", delimiter=",")
froutes = pd.read_csv("routes.txt", delimiter=",")
fstop_times = pd.read_csv("stop_times.txt", delimiter=",")
fstops = pd.read_csv("stops.txt", delimiter=",")

#Anthony's code

trips = ftrips
stop_times = fstop_times
stops = fstops
routes = froutes
#trips = trips[trips.service_id == service_id]
trips = trips.merge(routes[['route_id', 'route_short_name']], on=['route_id'])
route_stops = stop_times.merge(trips[['trip_id', 'direction_id', 'block_id', 'route_short_name', 'service_id']],  # removed route_id **
                               on=['trip_id'])
route_stops = route_stops.merge(stops[['stop_id', 'stop_lat', 'stop_lon']])

#Only looking for Route 5 Southbound gtsf times and coordinates
gtsf_5_Southbound = route_stops.loc[(route_stops['route_short_name'] == "5") & (route_stops['direction_id'] == 1)]
gtsf_5_Southbound.to_excel("gtsf_5_Southbound.xlsx")