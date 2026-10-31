#------------------------------------------------------------------
# ArgosSelectionTool.py
#
# Description: Reads in an Argos tracking data file and allows 
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: Elizabeth Miles-Flynn (elizabeth.miles-flynn@duke.edu)
# Date: 10/5/2026
#-------------------------------------------------------------------

# ——————————————————————————————————————————————————————————————————
# VERSION 1: Parse a single line of tracking data and report if the track point falls within the box
# ——————————————————————————————————————————————————————————————————
# Create the geographic selection box
the_box = {
    'x_min': 34.00,
    'y_min': -76.00,
    'x_max': 34.50,
    'y_max': -75.00}

# Copy and paste a line of data as the lineString variable value
lineString = "10154641232,'true',2019-5-14 13:37:52.000,-75.49356999999998,34.86216,0.0,-127.0,4.0167976787E8,5141.0,424,'40',34.86216,34.86216,'0',-75.49356999999998,-75.49356999999998,6,0,3,61.0,381.0,10718.0,2466.0,150,187,2,0,'1','argos-doppler-shift','Pterodroma hasitata','174441','HA09','Satellite tracking of black-capped petrels', 2019"

# Use the split command to parse the items in lineString into a list object
line_data = lineString.split(',')

# Assign variables to specific items in the list
event_id = line_data[0]          # Argos tracking event ID ("event-id")
timestamp = line_data[2]         # Observation date ("timestamp")
lat = float(line_data[3])               # Observation latitude ("location-lat")
lon = float(line_data[4])               # Observation longitude ("location-lon")
lc = line_data[14]                # Observation location class ("argos:lc")
tag_id = line_data[-3]            # Tag identifier ("tag-local-identifier")

# Print information to the use
    #print (f"Record {event_id} indicates {tag_id} was seen at {lat}N and {lon}W on {timestamp}")

# Evaluate latitude and longitude conditions
lat_condition = the_box['y_min'] < lat < the_box['y_max']
lon_condition = the_box['x_min'] < lon < the_box['x_max']

    #print(lat_condition)
    #print(lon_condition)

# Report the status of the points
if lat_condition & lon_condition:
    print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
else:
    print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')

# ——————————————————————————————————————————————————————————————————
# VERSION 2: Read the data directly from the Argos data file
# ——————————————————————————————————————————————————————————————————
# Create a variable pointing to the data file
file_name = 'Data/Raw/Satellite tracking of black-capped petrels 2019-argos.csv'

# Read the contents of the file into a list of lines
with open(file_name,'r') as f:
    # Read contents of file into a list
    line_list = f.readlines()

# Pretend we read one line of data from the file
lineString = line_list[200]

# Use the split command to parse the items in lineString into a list object
line_data = lineString.split(',')

# Assign variables to specific items in the list
event_id = line_data [0]     # Argos tracking event ID ("event-id")
timestamp = line_data [2]    # Observation date ("timestamp")
lat = float(line_data [4])   # Observation latitude ("location-lat")
lon = float(line_data [3])   # Observation longitude ("location-lon")
lc = line_data [14]          # Observation location class ("argos:lc")
tag_id = line_data [-3]      # Tab identifier ("tag-local-identifier")

# Evaluate latitude and longitude conditions
lat_condition = the_box['y_min'] < lat < the_box['y_max']
lon_condition = the_box['x_min'] < lon < the_box['x_max']

# Report the status of the points
if lat_condition & lon_condition:
    print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
else: 
    print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')

# ——————————————————————————————————————————————————————————————————
# VERSION 3: Process all lines in the Argos file using a FOR loop
# ——————————————————————————————————————————————————————————————————
# Loop through all the lines
for lineString in line_list[1:]:
    # Use the split command to parse the items in lineString into a list object
    line_data = lineString.split(',')

    # Assign variables to specific items in the list
    event_id = line_data [0]     # Argos tracking event ID ("event-id")
    timestamp = line_data [2]    # Observation date ("timestamp")
    lat = float(line_data [4])   # Observation latitude ("location-lat")
    lon = float(line_data [3])   # Observation longitude ("location-lon")
    lc = line_data [14]          # Observation location class ("argos:lc")
    tag_id = line_data [-3]      # Tab identifier ("tag-local-identifier")

# Evaluate latitude and longitude conditions
    lat_condition = the_box['y_min'] < lat < the_box['y_max']
    lon_condition = the_box['x_min'] < lon < the_box['x_max']

   # Report the status of the points
    if lat_condition & lon_condition:
        print(f'Record {event_id}: {tag_id} was IN the box at {timestamp}')
    else:
        print(f'Record {event_id}: {tag_id} was NOT IN the box at {timestamp}')
 