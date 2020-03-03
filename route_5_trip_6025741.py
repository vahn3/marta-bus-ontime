import pandas as pd
ftrips = pd.read_csv("trips.txt", delimiter=",")
froutes = pd.read_csv("routes.txt", delimiter=",")
fstop_times = pd.read_csv("stop_times.txt", delimiter=",")
fstops = pd.read_csv("stops.txt", delimiter=",")

trips = ftrips
stop_times = fstop_times
stops = fstops
routes = froutes
#trips = trips[trips.service_id == service_id]
trips = trips.merge(routes[['route_id', 'route_short_name']], on=['route_id'])
route_stops = stop_times.merge(trips[['trip_id', 'direction_id', 'block_id', 'route_short_name', 'service_id']],  # removed route_id **
                               on=['trip_id'])
route_stops = route_stops.merge(stops[['stop_id', 'stop_lat', 'stop_lon']])

route_5 = route_stops.loc[(route_stops['route_short_name'] == "5")] #extract route 5 from combined gtsf
route_5_trip_6025741 = route_5.loc[(route_5['trip_id'] == 6025741)] #selected trip_id 6025741
data = route_5_trip_6025741
#route_5_trip_6025741[['departure_time', 'stop_sequence', 'stop_id', 'stop_lat', 'stop_lon']]
#trimmed down to arrival_time, departure_time, stop_id, stop_lat_, stop_long

datatoexcel = pd.ExcelWriter("route5_trip6025741.xlsx", engine = 'xlsxwriter')
data.to_excel(datatoexcel, sheet_name = 'Sheet1')
datatoexcel.save()