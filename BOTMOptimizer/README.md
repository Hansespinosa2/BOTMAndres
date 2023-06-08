# BOTMAndres

Bread of the Mighty Repository with separated files based off the working version notebook previously set up in Google Colab

Brief description of each file, their purposes, and any to-do items to go with them:

 - Init file, initialize the variables. TODO: See if the variables set up in main.py could set up here for cleaner code
 - coordinates.py, this asks coordinates for new locations. TODO: Ported over from the notebook but serves no function in this code
 - create_map.py, this will create a map of optimized routes for the week. TODO: If any new map interactions or set ups want to be done, this is the file to do them in.
 - dataframe.py, creates dataframe from worksheet. TODO: This is very basic but can be expanded on to push data to the fire database when established
 - geocoding.py, set of location functions. TODO: Understand how it can be used for further optimization
 - google_sheets.py, connects to the sheets and credentials.json file. TODO: Currently must be edited in order to replace the directory with the specified directory in any computer. Should be changed to allow for easy input changes by the user for the directory of the credentials file. 
 - main.py, runs the package. TODO: Move set up variables and see other areas for improvement
 - optimize.py, optimizer function. TODO: Not much area for optimization
 - routes.py, sets up days for each route and returns a dataframe for the week. TODO: add connectivity to fire database
 - setup.py, set up for a package distribution. TODO: Actually set it up for package distribution.
 - vehicle_pickups.py Sets up the pickups and vehicle definitions. TODO: Investigate if the vehicles can be expanded upon for each vehicle and their capacity.
