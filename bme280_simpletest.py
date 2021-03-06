 
import datetime 
import time
import math 
import board 
import busio 
import adafruit_bme280
 
# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)
 
# OR create library object using our Bus SPI port
# spi = busio.SPI(board.SCK board.MOSI board.MISO)
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi bme_cs)

now = datetime.datetime.now()


b = 17.62
c = 243.12
gamma = (b * bme280.temperature /(c + bme280.temperature)) + math.log(bme280.humidity / 100.0)
cdewpoint = (c * gamma) / (b - gamma)

fr = 32 
s = 1.8
cdeg = bme280.temperature
# Temp in Ferinhight
fdeg = (cdeg * s) + fr
# DewPoint in Ferinhight
ddewpoint = (cdewpoint * s) + fr

# Humidity
relhumid = bme280.relative_humidity
# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1019.989

while True:
        istime = (time.strftime('%X'))
        ctemp = "%0.2f C" % cdeg
        ftemp = "%0.2f F" % fdeg
        hmid = ("%0.2f %%" % bme280.relative_humidity)
        hpa = ("%0.6f hPa" % bme280.pressure)
        altitude = ("%0.2f meters" % bme280.altitude)
        cdew = ("%0.2f dew-C" % cdewpoint)
        fdew = ("%0.2f dew-F" % ddewpoint)
        datapoint = [istime,ctemp,ftemp,hmid,hpa,altitude,cdew,fdew]
        print(datapoint)
        time.sleep(1)
