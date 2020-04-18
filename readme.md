# simulation.py 
This is a simulation to model the spread of COVID-19.  

You can turn visualization on or off from the configuration file.  

## Settings file
The program expects a file called settings.txt in the same directory as the corona.py
You can make comments with the #.  

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

## Running the simulation program

From the console type python corona.py

This generates a csv file with results that should be opened with excel, sheets, or similar.  

## Plotting using the matplotlib program

From the console type python plot.py 

A graph should appear.  A pdf of the graph is also created.  

<object data="https://github.com/bradfletcher/covid/blob/master/figure1.pdf" type="application/pdf" width="700px" height="700px">
    <embed src="https://github.com/bradfletcher/covid/blob/master/figure1.pdf">
        <p>This browser does not support PDFs. Please download the PDF to view it: <a href="https://github.com/bradfletcher/covid/blob/master/figure1.pdf">Download PDF</a>.</p>
    </embed>
</object>

## Methodology
This model contains 2 entities, people and locations.  

Person

Location

When the sim starts people are placed in random locations, however the capacity of a location is respected.  That means if the random location is a business, and a business has a max capacity of 10, and there are currently 10 people there a new location for the person is selected.  

If the location contains at least one infected person the location is infected and anyone visiting has a chance of becoming infected.  The chance is set by chanceOfTransmission.

The time resolution of the sim is hourly.  Each hour all people are iterated over and there is a chance of moving.  

## Simplifications 
People are assumed to always be at some location.  There is no chance that someone can be infected while in transit.  