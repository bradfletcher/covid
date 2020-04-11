# simulation.py 
This is a simulation to model the spread of COVID-19.  

You can turn visualization on or off from the configuration file.  

## Settings file
The program expects a file called settings.txt in the same directory as the corona.py

Here is an example:

population 5000

visualization False 

width 1800 

height 1000 

weeks 8

businesses 500

homes 300

schools 50

hoursToRecover 240 

chanceOfTransmission 1 

chanceOfMoving 2 


For chance of transmission and chance of moving these integers represent a percentage, so 1 means 1% chance, and 5 means a 5 percent chance.  

## Running the program

From the console type python corona.py

This generates a csv file with results that should be opened with excel, sheets, or similar.  

## Methodology
This model contains 2 entities, people and locations.  

Person

Location

## Simplifications 
People are assumed to always be at some location.  There is no chance that someone can be infected while in transit.  