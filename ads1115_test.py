import board
import busio
import adafruit_ads1x15.ads1015 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
import time

# i2c configuration
i2c = busio.I2C(board.SCL, board.SDA)
# Create the ADC object using the I2C bus
ads = ADS.ADS1015(i2c)
# Create input on channel 0, 1, 2, 3
chan_1 = AnalogIn(ads, ADS.P0)
chan_2 = AnalogIn(ads, ADS.P1)
chan_3 = AnalogIn(ads, ADS.P2)
chan_4 = AnalogIn(ads, ADS.P3)

while True:
    print("CH0: %f CH1: %f CH2: %f CH3: %f" % (chan_1.voltage, chan_2.voltage, chan_3.voltage, chan_4.voltage))
    time.sleep(0.1)
