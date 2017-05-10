import logging, mcp3002
from weather_station.WeatherInstruments.WeatherInstrumentClass import WeatherInstrument

class WindDirectionSensor(WeatherInstrument):

    
    def __init__(self, json):
        super().__init__(json)
        print("I am a wind direction sensor")
        self.__ADC = self._getADC()


    def getData(self):
        myData = {"winddir": self.getWindDirection()}
        logging.info("The wind direction data is %s" % str(myData))
        return myData
    

    def getWindDirection(self):
        #  Fill in code here that actually gets the wind direction.
        sensorVoltage = self.__ADC.readChannel0()
        windDirection = sensorVoltage * 72
        return windDirection        
    

    def _getADC(self):
        # Return an Analog to Digital converter object
        return mcp3002.MCP3002()
        


if __name__ == "__main__":
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    wds = WindDirectionSensor("Hello")
    print(str(wds.getData()))
