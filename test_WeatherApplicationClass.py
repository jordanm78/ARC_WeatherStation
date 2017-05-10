from weather_station.WeatherApplicationClass import WeatherApplication
from weather_station.test_weatherstation import test_WeatherStation
import logging

class test_WeatherApplication(WeatherApplication):

    def _getWeatherStation(self):
        return test_WeatherSTation()
        


if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    twa = test_WeatherApplication()
