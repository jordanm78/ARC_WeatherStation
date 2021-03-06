from tkinter import Tk, Frame, Button, ttk, LEFT, RIGHT, BOTH, X, Y  #Import classes and constants for the user interface.
from tkinter import *
import serial #This is the class that is needed to communicate over the serial port.  It comes from the PySerial package.
import time, datetime
import RPi.GPIO as GPIO
import requests
import logging



class WeatherStation(Frame):  #Define a new class that inherits from the Frame class
  
  def __init__(self, parent):
    Frame.__init__(self, parent)   
    self.parent = parent

    #  Set up logging
    logging.basicConfig(level=logging.WARNING, #Levels are DEBUG, INFO, WARNING, ERROR, CRITICAL
                    format='%(asctime)s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='WeatherStationLog.log',
                    filemode='w')

    #  Set up the GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(2, GPIO.IN) 


    #  Set up the Serial Port
    #ser = serial.Serial()  # open serial port
    #ser.baudrate = 38400   # Set the baud rate
    #ser.port = 'COM3'  #'/dev/ttyAMA0'      # Set the serial port.  'COM4' in windows, '/dev/ttyUSB0' in linux.
    #ser.open()             # Open the serial port
    #self.serial = ser      # Retain a reference to the serial port


    #Call the initUI method
    self.initUI()  
        




  #Initialize the user interface
  def initUI(self):  
    self.parent.title("Weather Station")
    self.configure(bg = "white")
    self.pack(fill=BOTH, expand=1)

    #---Define some variables
    self.windSpeed = 0
    self.windSpeedString = StringVar()
    self.windSpeedString.set('0')
    self.weatherData = ""

    self.numberOfChecks = 0

    self.previousRisingEdgeTime=time.time()

    self.previousVoltage=1



    

    #---Wind Speed Label

    # Create and configure a wind speed label
    windSpeedLabel = Label(self, text = "Wind Speed (MPH)", bg = "white", fg = "blue", font = ("Helvetica", 24))

    #Place the label in the window
    windSpeedLabel.pack(fill = X, padx = 5, pady = 5)  #Make the entry stretch to fill the window in the X direction, with 5 pixels of padding on the tops and sides.


     
    #---Wind Speed Indicator

    # Create and configure a wind speed indicator
    windSpeedIndicator = Label(self, textvariable = self.windSpeedString, bg = "white", fg = "blue", font = ("Helvetica", 24))

    #Place the label in the window
    windSpeedIndicator.pack(fill = X, padx = 5, pady = 5)  #Make the entry stretch to fill the window in the X direction, with 5 pixels of padding on the tops and sides.




    #---Quit Button
        
    # Create and configure a quit button
    quitButton = Button(self, text="Quit", command=self.quit, height = 2)


    #Place the button in the window
    quitButton.pack(padx = 5, pady = 5)  #Make the button stretch to fill the window in the X direction, with 5 pixels of padding on the tops and sides.




    #---Start the repeating functions
    self.checkWindSpeed()
    self.mainWeatherLoop()

  #This is what happens when Clockwise button gets pressed
  def clockwiseButtonPressed(self):
    message = 'clockwise'                   #Create a message to send
    byteMessage = message.encode('UTF-8')   #Convert the message to bytes, which can be sent over the serial port
    self.serial.write(byteMessage)          #Send the message over the serial port


  #This is what happens when Counterclockwise button gets pressed
  def counterclockwiseButtonPressed(self):
    message = 'counterclockwise'            #Create a message to send
    byteMessage = message.encode('UTF-8')   #Convert the message to bytes, which can be sent over the serial port
    self.serial.write(byteMessage)          #Send the message over the serial port



  def getWeatherData(self):
    logging.debug("The windspeed is %s" % str(self.windSpeed))
    self.weatherData = {'ID':'KCASACRA194',
               'PASSWORD':'yxhczp7r',
               'dateutc': 'now',
               'realtime': '1',
               'rtfreq': '2.5',         
               'action':'updateraw',
               'windspeedmph':self.windSpeed}


    
  def updateWeatherUndergroundPage(self):

    try:  #Try to send a "get" request to the weather undergound website.  Include the parameters.
      r = requests.get('https://rtupdate.wunderground.com/weatherstation/updateweatherstation.php',
                     params = self.weatherData)

    #Catch and handle any connection error.
    except requests.exceptions.ConnectionError as error:
      logging.exception("The following connection error occurred while trying to connect to the weather underground website: %s"
                        % str(error))

    #Catch and handle any other error.
    except requests.exceptions.RequestException as error:
      logging.exception("The following unknown error occurred while trying to connect to the weather underground website: %s"
                        % str(error))
      
    else:
      #There was no error, so log the website and the response.
      logging.info("I went to the weather underground url: %s" % str(r.url))  #Print the url that was generated by the get request
      logging.info("The wunderground response was: %s" % str(r.text)) #Print the response that we got from the website.  This should be "success".


  def mainWeatherLoop(self):
    self.getWeatherData()
    self.updateWeatherUndergroundPage()
    self.parent.after(2500, self.mainWeatherLoop)   

  
  #This method checks the wind speed
  def checkWindSpeed(self):
    #self.windSpeed.set(GPIO.input(26))
    #print (GPIO.input(26))
    if self.checkRisingEdge():
      self.windSpeed = self.calculateWindSpeed()
    else:
      self.windSpeed = self.windSpeed * .999
    self.windSpeedString.set("%.1f" %self.windSpeed)
    self.parent.after(10, self.checkWindSpeed)
    
  #This method calculates the wind speed
  def calculateWindSpeed(self):
    now = time.time()
    #print(now)
    timeBetweenEdges= now - self.previousRisingEdgeTime
    edgeFrequency=1/timeBetweenEdges
    windspeed=1.677*edgeFrequency+.4
    
    self.previousRisingEdgeTime=now
    #print(windspeed)
    return windspeed
   
  #This method checks for rising edge
  def checkRisingEdge(self):
    presentVoltage=GPIO.input(2)
    #print("Present Voltage: ", presentVoltage, ".  Previous voltage: ", self.previousVoltage)
    if presentVoltage == 1 and self.previousVoltage == 0:
      risingEdgeFound=True
    else:
      risingEdgeFound=False
    self.previousVoltage=presentVoltage
    #print(risingEdgeFound)
    return risingEdgeFound



  #This method quits the program
  def quit(self):
    #self.serial.close()
    self.parent.destroy()


        


def main():
  
  root = Tk()
  app = WeatherStation(root)
  root.mainloop()  




if __name__ == '__main__':
    main()


