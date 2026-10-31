#------------------------------------------------------------------
# ReadArgosDataFile.py
#
# Description: Reads in an Argos tracking data file and allows 
#   the user to identify the tracked sitings found within a 
#   specified bounding box.
#
# Author: Elizabeth Miles-Flynn (elizabeth.miles-flynn@duke.edu)
# Date: 10/30/2026
#-------------------------------------------------------------------

# Set a variable to the CSV filename
the_filename = 'Data/Raw/Satellite tracking of black-capped petrels 2019-argos.csv'
# Create a file object pointing to file name
f = open(the_filename,'r')

# Create a list of all the lines in the file via the file object
line_list = f.readlines()
# Close the file
f.close()
# Print the 11th item in the line list
print(line_list[10])

# WITH keyword when need object temporarily in script
with open('Data/Raw/Satellite tracking of black-capped petrels 2019-argos.csv', 'r') as f:
    line_list = f.readlines()
print(line_list[10])