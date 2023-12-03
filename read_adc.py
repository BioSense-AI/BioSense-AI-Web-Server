import wiringpi


PINBASE= 1
I2CADDRESS = 0x34

wiringpi.ads1115Setup(PINBASE, I2CADDRESS)

wiringpi.wiringPiSetup() # Initialize WiringPi library
fd = wiringpi.wiringPiI2CSetup(0x48) # Initialize I2C interface with ADS1115 address (0x48)
if fd == -1:
    # Handle error if I2C initialization fails
    exit(1)

# Read the ADS1115 value
value = wiringpi.wiringPiI2CReadReg16(fd, 0x00)
if value < 0:
    # Handle error if reading fails
    exit(1)

# Convert the value to voltage
voltage = value * 0.1875 # Assuming full-scale range of +/- 4.096V

# Print the voltage value
print("ADS1115 Value: {} V".format(voltage))