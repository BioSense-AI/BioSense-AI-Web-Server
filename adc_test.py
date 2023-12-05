import time
import Adafruit_ADS1x15
# import json

# Create an ADS1115 ADC (16-bit) instance.
adc = Adafruit_ADS1x15.ADS1115(address=0x48,busnum=2)

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print(' ')
# Print nice channel column headers.
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)

# Main loop.
while True:
    # reading from a0 pin
    a0 = adc.read_adc(0,gain=GAIN)
    # Read all the ADC channel values in a list.
    # values = [0]*4
    # for i in range(4):
        # Read the specified ADC channel using the previously set gain value.
        # values[i] = adc.read_adc(i, gain=GAIN)
        # Note you can also pass in an optional data_rate parameter that controls
        # the ADC conversion time (in samples/second). Each chip has a different
        # set of allowed data rate values, see datasheet Table 9 config register
        # DR bit values.
        # values[i] = adc.read_adc(i, gain=GAIN, data_rate=128)
        # Each value will be a 12 or 16 bit signed integer value depending on the
        # ADC (ADS1015 = 12-bit, ADS1115 = 16-bit).
    # Print the ADC values.
    # print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
    print(f'|{a0}|')
    # Pause for half a second.
    time.sleep(0.5)

# import time
# import board
# import busio
# import adafruit_ads1x15.ads1115 as ADS
# from adafruit_ads1x15.analog_in import AnalogIn

# # Create the I2C bus
# # i2c = busio.I2C()

# # Create the ADC object using the I2C bus
# ads = ADS.ADS1115(i2c)

# # Create single-ended input on channel 0
# chan = AnalogIn(ads, ADS.P0)

# # Create differential input between channel 0 and 1
# #chan = AnalogIn(ads, ADS.P0, ADS.P1)

# print("{:>5}\t{:>5}".format('raw', 'v'))

# while True:
#     print("{:>5}\t{:>5.3f}".format(chan.value, chan.voltage))
#     time.sleep(0.5)