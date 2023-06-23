import pandas as pd
import plotly.express as px
from IPython.display import display
import os
import datetime

import dash
from dash  import dcc
from dash import html
from dash.dependencies import Input, Output


file_path = "./data/"
folder_names = [f for f in os.listdir(file_path) if os.path.isdir(os.path.join(file_path, f))]
agency_df = None
stops_df = None
routes_df = None
trips_df = None
stop_times_df = None

for folder_name in folder_names:
    print(folder_name)
    try:
        #agency
        new_agency_df = pd.read_csv(file_path + folder_name + "/agency.txt")
        new_agency_df["date"] = folder_name
        agency_df = pd.concat([agency_df, new_agency_df], ignore_index=True)

        #stops
        new_stops_df = pd.read_csv(file_path + folder_name + "/stops.txt")
        new_stops_df["date"] = folder_name
        stops_df = pd.concat([stops_df, new_stops_df], ignore_index=True)

        #routes
        new_routes_df = pd.read_csv(file_path + folder_name + "/routes.txt")
        new_routes_df["date"] = folder_name
        routes_df = pd.concat([routes_df, new_routes_df], ignore_index=True)

        #trips
        new_trips_df = pd.read_csv(file_path + folder_name + "/trips.txt")
        new_trips_df["date"] = folder_name
        trips_df = pd.concat([trips_df, new_trips_df], ignore_index=True)

        #stop_times
        new_stop_times_df = pd.read_csv(file_path + folder_name + "/stop_times.txt")
        new_stop_times_df["date"] = folder_name
        stop_times_df = pd.concat([stop_times_df, new_stop_times_df], ignore_index=True)
        
    except ValueError:
        print("Error")


stops_df['date'] = pd.to_datetime(stops_df['date'], format='%Y%m%d')
agency_df["date"] = pd.to_datetime(agency_df['date'], format='%Y%m%d')
routes_df["date"] = pd.to_datetime(routes_df['date'], format='%Y%m%d')
trips_df["date"] = pd.to_datetime(trips_df['date'], format='%Y%m%d')
stop_times_df["date"] = pd.to_datetime(stop_times_df['date'], format='%Y%m%d')

print("salva")
stops_df.to_csv("stops_df.csv", index = False)
agency_df.to_csv("agency_df.csv", index = False)
routes_df.to_csv("routes_df.csv", index = False)
trips_df.to_csv("trips_df.csv", index = False)
stop_times_df.to_csv("stop_times_df.csv", index = False)
print("terminato")