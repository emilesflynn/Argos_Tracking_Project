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
the_filename = 'data/raw/MoveBank/Satellite tracking of black-capped petrels 2019-argos.csv'
# Create a file object pointing to file name
f = open(the_filename,'r')