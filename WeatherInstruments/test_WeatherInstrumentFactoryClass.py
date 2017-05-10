from weather_station.WeatherInstruments.ConcreteWeatherInstruments.testInstruments import test_Anemometer, test_WindDirectionSensor
from weather_station.WeatherInstruments.WeatherInstrumentFactoryClass import WeatherInstrumentFactory
import json
import inspect
import logging


class test_WeatherInstrumentFactory(WeatherInstrumentFactory):


    def createWeatherInstruments(self):
        #This method creates and returns a list of test weather instruments

        #Create an empty list to hold the weather sensors 
        weatherSensorList = []

        #This line creates a test_Anemometer and adds it to the list
        weatherSensorList.append(test_Anemometer.test_Anemometer(json))


        #This line creates a test_WindDirectioniSensor and adds it to the list
        weatherSensorList.append(test_WindDirectionSensor.test_WindDirectionSensor(json))

        logging.info("The completed weather sensor list is %s" % str(weatherSensorList))         
        return weatherSensorList
        
        

if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    twif = test_WeatherInstrumentFactory()
    twif.createWeatherInstruments()
