import logging
import test_mcp3002
import sys
from weather_station.WeatherInstruments.ConcreteWeatherInstruments.WindDirectionSensorClass import WindDirectionSensor

class test_WindDirectionSensor(WindDirectionSensor):

    
    def __init__(self, json):
        super().__init__(json)
        print("I am a dummy wind direction sensor")


    def _getADC(self):
        # Return an Analog to Digital converter object
        logging.debug("The test_WindDirectionSensor._getADC method has been called")
        return test_mcp3002.Test_MCP3002()
        


if __name__ == "__main__":
    
    logging.basicConfig(filename='WeatherUndergroundClass.log', level=logging.DEBUG)
    twds = test_WindDirectionSensor("Hello")
    print(str(twds.getData()))
