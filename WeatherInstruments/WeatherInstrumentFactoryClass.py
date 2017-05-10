from weather_station.WeatherInstruments.ConcreteWeatherInstruments import AnemometerClass, WindDirectionSensorClass
import json
import inspect
import logging


class WeatherInstrumentFactory(object):

    def __init__(self):
        pass


    def createWeatherInstruments(self):

        """
        This method should follow the chain of responsibility pattern.
        reads a config file, creates a
        weather instrument for each entry in the config
        file, and returns a list of weather instruments.
        """

        """
        For now, this method just creates the objects and returns them.

        """
        configData = self.getConfigData()

        weatherInstrumentList = {}


    def getConfigData(self):
        #This method loads the configuration data for the weather instruments
        #Open the configuration file and create a list of instrument configuration objects
        return "config data"
        

        

        
if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    WeatherInstrumentFactory.createWeatherInstruments("Hello")
