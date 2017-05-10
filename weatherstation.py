from weather_station.WeatherInstruments import WeatherInstrumentFactoryClass
import logging

class WeatherStation(object):

    def __init__(self):
        #This method will create all of the instruments and store them for future use
        wif = self._getWeatherInstrumentFactory()
        self.weatherInstrumentList = wif.createWeatherInstruments()


    def start(self):
        #This method will start all of the instruments
        #This method should also start an asynchronous loop that updates weather underground.
        for instrument in self.weatherInstrumentList:
            instrument.start()


    def stop(self):
        #This method will stop all of the instruments
        for instrument in self.weatherInstrumentList:
            instrument.stop()


    def getData(self):
        #This method will return the data from all of the instruments
        weatherData = {}
        for instrument in self.weatherInstrumentList:
            instrumentData = instrument.getData()
            logging.info("I have gotten the following instrument data: %s" % str(instrumentData))
            weatherData.update(instrumentData)

        logging.info("The final weather data is %s" % str(weatherData))
        return weatherData
    

    def _getWeatherInstrumentFactory(self):
        #This method will return a weather instrument factory.
        #This method can be overridden by a child test class,
        #to return a test instrument factory.
        return WeatherInstrumentFactoryClass.WeatherInstrumentFactory()
