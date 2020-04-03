import folium
import pandas as pd

#read in the Google Sheets called route5_on_time_performance
data = pd.read_csv("route5_performance_4_1.csv")
#Goal: for every row, make a tuple of (latitude, longitude) + other details --> giant list of info per stop

other_coordinate_info = []
for index, row in data.iterrows(): 
    tuples = (row['stop_lat'], row['stop_lon'])
    stop = {tuples, row['stop_id'], row['actual_time'], row['departure_time'], row['difference'], row['stop_name']}
    other_coordinate_info.append(stop)
    
#other_coordinate_info contain: (lat, long), stop_id, number of times, average on-time, stop_name

#Create a base map using coordinates of Atlanta
m = folium.Map(location=[33.7490, -84.3880])

#add markers
for stop in other_coordinate_info:
    #info = 'stop_id: {}, stop_name: {}, avg_ontime_seconds: {}'.format(stop['stop_id'], stop['stop_name'], stop['difference'])
    if stop['difference'] > 600:
        folium.Marker(stop[0], popup = info, icon=folium.Icon(color='black')).add_to(m)
    if ((stop['difference'] < 600) & (stop['difference'] >= 300)):
        folium.Marker(stop[0], popup = info, icon=folium.Icon(color='red')).add_to(m)
    if ((stop['difference'] < 300) & (stop['difference'] >= 0)): 
        folium.Marker(stop[0], popup = info, icon=folium.Icon(color='white')).add_to(m)
    if ((stop['difference'] > -300) & (stop['difference'] < 0)): 
        folium.Marker(stop[0], popup = info, icon=folium.Icon(color='blue')).add_to(m)
    if ((stop['difference'] > -600) & (stop['difference'] < -300)): 
        folium.Marker(stop[0], popup = info, icon=folium.Icon(color='orange')).add_to(m)

m.save('data_4_1')