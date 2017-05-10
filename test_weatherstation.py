import logging
from weather_station.weatherstation import WeatherStation
from weather_station.WeatherInstruments.test_WeatherInstrumentFactoryClass import test_WeatherInstrumentFactory 



class test_WeatherStation(WeatherStation):


    def _getWeatherInstrumentFactory(self):
        #This method will return a test weather instrument factory.
        return test_WeatherInstrumentFactory()



if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    tws = test_WeatherStation()


    #Start the application
    tws.start()


    #read and print the data 5 times
    for i in range(5):
        print(tws.getData())


    #stop the application
    tws.stop()
    
