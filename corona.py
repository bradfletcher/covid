from graphics import * 
from random import seed
from random import randint
from datetime import datetime 
import time 

# seed random number generator
seed(datetime.now)
# generate some integers

# locations have the following properties
# capacity
# type - home, essential business, non-essentail business, school 

# people
# currently_infected t/f
# recovered t/f 
# hospitalized t/f 

# parameters for the simulation that can vary 
# probably that if two people were at the same location that disease was spread 
chanceOfTransmission = .1
# days until infected person recovers and is not longer contegios 
hoursToRecover = 72  
totalInfected = 1 
recovered = 0 
dead = 0 

# how many people in the city
population = 500 
businesses = 10
schools = 5
homes = 30
weeks = 1 

# turn visuals on or off 
visualization = False 

# graphics params 
# width 
width = 1400
height = 800

if (visualization ): 
    win = GraphWin('Simulation', width, height) # give title and dimensions

class Person:
  def __init__(self, currently_infected, days_infected, alive, recovered, hospitalized, age, marker, markerDrawn, location, x, y):
    self.currently_infected = currently_infected
    self.days_infected = days_infected 
    self.alive = alive
    self.recovered = recovered
    self.hospitalized = hospitalized
    self.age = age 
    self.marker = marker
    self.markerDrawn = markerDrawn 
    self.location = location 
    self.x = x
    self.y = y 

class Location:
    def __init__(self, capacity, kind, open, x, y, numPeople, people, infected , marker, markerDrawn):
        self.capacity = capacity 
        self.kind = kind 
        self.open = open 
        self.x = x
        self.y = y 
        self.numPeople = numPeople 
        self.people = people 
        self.infected = infected 
        self.marker = marker 
        self.markerDrawn = markerDrawn 

#initial setup of locations 
locations = []
for l in range(businesses):
    x = randint(0, width) 
    y = randint(0, height) 
    locations.append(Location(25, "Essential Business", True,x , y , 0, [], False, Circle(Point(x,y), 8), False)) 
for l in range(schools):
    x = randint(0, width) 
    y = randint(0, height) 
    locations.append(Location(1000, "School", True, x, y, 0, [] , False ,  Circle(Point(x,y), 50), False)) 
for l in range(homes):
    x = randint(0, width) 
    y = randint(0, height) 
    locations.append(Location(4, "Home", True, x, y , 0, [] , False ,  Circle(Point(x,y), 12), False )) 

#create a file to record population stats 
f = open("stats.csv", "w")
f.write("Hours"  + "," ) 
f.write("Infected" + ",") 
f.write("Recovered" + "," ) 
f.write("Dead" ) 
f.write("\n"); 

#initial setup of people 
def whereIsPerson():
    numberOfLocations = len(locations) 
    locate = locations[randint(0,numberOfLocations - 1 ) ] 
    while(locate.numPeople >= locate.capacity):
        locate = locations[randint(0,numberOfLocations - 1 ) ] 
    return locate 

people = []

for x in range(population):
    loc = Location(4, "null", True, 0, 0 , 0, [] , False ,  Circle(Point(0,0), 12), False )
    per1 = Person(False, 0, True, False,False, 25, Circle(Point(0,0 ), 2 ), False, loc, 0, 0) 
    locale = whereIsPerson()
    per1.location = locale 
    locale.people.append(per1) 
    locale.numPeople += 1
    if (locale.kind == "School"):
        randHor = randint(0,60) - 30
        randVert = randint(0, 60) - 30 
    else: 
        randHor = randint(0,10) - 5
        randVert = randint(0,10) - 5 

    per1.marker = Circle(Point(locale.x + randHor, locale.y + randVert ), 2 ) 
    per1.x = locale.x + randHor 
    per1.y = locale.y + randVert 
    people.append(per1)

people[0].currently_infected = True 

def redraw():
    for l in locations:
        circ = l.marker 
        if(l.kind == "Home" ):
            # print("home" )
            circ.setFill("green")
        elif (l.kind == "School" ):
            # print("school" )
            circ.setFill("pink") 
        else:
            circ.setFill("yellow")
        
        if (l.markerDrawn == False ): 
            if (visualization ) :
                circ.draw(win)
            l.markerDrawn = True 

    for p in people:
        if(p.markerDrawn == False ) : 
            circ = p.marker 
            if(p.currently_infected == False ) :
                circ.setFill("blue")
            else:
                circ.setFill("red")
                circ.setOutline("red")
            if(visualization ) : 
                circ.draw(win) 
            p.markerDrawn = True 

def formatTime(hours ):
    if (hours < 24 ):
        return str(hours) + " Hours" 
    else:
        return str(hours // 24) + " Days " + str( hours % 24 ) + " Hours"  


def move() : 
    for p in people:
        chanceOfMoving = randint(0, 99 ) 
        if (chanceOfMoving < 5 ) : 
            # move the person 
            locationCur = p.location 
            locationCur.people.remove(p)
            locationCur.numPeople -= 1 
            # print("cur loc x: " + str(locationCur.x) + ", y: " + str(locationCur.y) ) 
            locationNew = whereIsPerson() 
            p.location = locationNew 
            locationNew.people.append(p)
            locationNew.numPeople =+ 1 
            # print("new loc x: " + str(locationNew.x) + ", y: " + str(locationNew.y) ) 
            if (locationNew.kind == "School"):
                randHor = randint(0,60) - 30
                randVert = randint(0, 60) - 30 
            else: 
                randHor = randint(0,10) - 5
                randVert = randint(0,10) - 5 
            dx = locationNew.x - p.x + randHor 
            dy = locationNew.y - p.y + randVert 
            # print("dx: " + str(dx) + " dy: " + str(dy) )
            p.marker.move(dx, dy )
            p.x = p.x + dx 
            p.y = p.y + dy 

# This is the simulation loop 
# It will iterate through each timestep here 
redraw() 
for t in range(0, 24*7* weeks ): 
    #update the timestamp 
    if(visualization ) : 
        message = Text(Point(win.getWidth()/2, win.getHeight() - 20 ), 'Time 0 days 0 hours '  )
        message.setText(formatTime(t))
        message.setSize(20)
        message.draw(win)

    #write to the stats file 
    f.write(str(t) + "," ) 
    f.write(str(totalInfected) + ",") 
    f.write(str(recovered ) + "," )
    f.write(str(dead ) )
    f.write("\n"); 


    #update the infection count  
    if(visualization ) : 
        message2 = Text(Point(win.getWidth() - 300  , win.getHeight() - 20 ), ' Infected '  )
        message2.setText("Infected " + str(totalInfected ) )
        message2.setSize(20)
        message2.setTextColor("red" ) 
        message2.draw(win)

        #update the infection count  
        message3 = Text(Point(200 , win.getHeight() - 20 ), ' Population '  )
        message3.setText("Population: " + str(population ) )
        message3.setSize(20)
        message3.setTextColor("blue" ) 
        message3.draw(win)

        message4 = Text(Point(win.getWidth() - 180 , win.getHeight() - 20 ), ' Recovered '  )
        message4.setText("Recovered: " + str( recovered ) )
        message4.setSize(20)
        message4.setTextColor("green" ) 
        message4.draw(win)

        message5 = Text(Point(win.getWidth() - 50  , win.getHeight() - 20 ), ' Dead '  )
        message5.setText("Dead: " + str( dead ) )
        message5.setSize(20)
        message5.draw(win)

    # time.sleep(.1) 
    
    #iterate over all the locations 
    for l in locations:
        #iterate over the people at each location 
        for p in l.people: 
            if (p.currently_infected == True ) : 
                p.days_infected += 1 
                if ( p.days_infected >= hoursToRecover ) : 
                    prob = randint(0, 99) 
                    if( prob < 2 ) :
                        p.alive = False 
                        dead += 1 
                    else : 
                        p.recovered = True 
                        p.currently_infected = False 
                        p.marker.setFill("purple") 
                        p.marker.setOutline("purple") 
                        recovered += 1 
                        totalInfected -= 1 

            #update people status 
            if(l.infected == True and randint(0, 99) > 95 and p.recovered == False ) : 
                if(p.currently_infected == False ):
                    totalInfected += 1 
                p.currently_infected = True  
                p.marker.setFill("red")
                p.marker.setOutline("red" )
            if(p.currently_infected ) : 
                l.infected = True 
                l.marker.setOutline("red") 

    #move people to new location or have them stay put 
    move()

    if(visualization ):         
        message.undraw()
        message2.undraw() 
        message3.undraw() 
        message4.undraw() 
        message5.undraw() 

f.close()

if(visualization ) : 
    win.getMouse()
    win.close()