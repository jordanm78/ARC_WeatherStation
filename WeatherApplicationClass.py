import logging

class WeatherApplication(object):

    def __init__(self):
        self.weatherStation = self.getWeatherStation()
        self.weatherUnderground = WeatherUnderground()

    def start(self):
        self.weatherStation.start()
        #Also start an asynchronous loop that updates weather underground periodically

    def stop(self):
        self.weatherStation.stop()
        #Also stop the asynchronous loop that udates weather underground.


    def getData(self):
        return self.weatherStation.getData()

    def _getWeatherStation(self):
        #This is a protected methd that can be overridden by child test classes.
        return WeatherStation()
    


if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    wa = WeatherApplication()
