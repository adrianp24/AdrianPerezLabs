from Lights import *
from Buzzer import *
from Displays import *
import time

class TrafficLight:
    def __init__(self):
        self.state = "red"
        self.timer = 0

    def startTimer(self, duration):
        self.timer = duration
        while self.timer > 0:
            print("Traffic light:", self.state)
            time.sleep(1)
            self.timer -= 1

    def setState(self, state):
        self.state = state

class PedestrianLight:
    def __init__(self):
        self.state = "don't walk"
        self.timer = 0

    def startTimer(self, duration):
        self.timer = duration
        while self.timer > 0:
            print("Pedestrian light:", self.state)
            time.sleep(1)
            self.timer -= 1

    def setState(self, state):
        self.state = state

class TrafficLightController:
    def __init__(self):
        self.trafficLight = TrafficLight()
        self.pedestrianLight = PedestrianLight()
    
    def run(self):
        display = LCDDisplay(sda=20, scl=21, i2cid = 0)
        while True:

            self.trafficLight.setState("*****RED*****")
            display.showText("****WALK****")
            self.trafficLight.startTimer(3)
            

            self.pedestrianLight.setState("****WALK****")
            self.pedestrianLight.startTimer(2)

            self.pedestrianLight.setState("*****DON'T WALK****")
            self.trafficLight.startTimer(5)
            display.showText("****STOP****")

            self.trafficLight.setState("****GREEN****")
            self.trafficLight.startTimer(5)

            self.trafficLight.setState("****YELLOW****")
            self.trafficLight.startTimer(2)

controller = TrafficLightController()
controller.run()

## LCD SCREEN IS FOR THE PEDESTRIAN 
## CONSOLE LOGGING BOTH PEDSTRIAN AND TRAFFIC LIGHT
