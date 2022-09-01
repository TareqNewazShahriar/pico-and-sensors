from machine import Pin, ADC
import time

def convert_to_celcius(sensor_value):
   conversion_factor = 3.3 / (65535)
   reading = sensor_value * conversion_factor
   temperature = 27 - (reading - 0.706)/0.001721
   return temperature

file = open ("temperature-data.csv", "a")
file.write("Time, Build-in, Thermistor, Humiture, Temperature DS18b20\n")
file.flush()

builtin_sensor = ADC(4)
thermistor_sensor = ADC(2)
humiture_sensor = ADC(1)
temperature_sensor = ADC(0)

delay = 60 * 5
temp_val = 0

print('ok')

while True:
   temp_val = temperature_sensor.read_u16()

   #print('build-in', convert_to_celcius(builtin_sensor.read_u16()), 'thermistor', thermistor_sensor.read_u16(), 'humiture', humiture_sensor.read_u16(), 'temperature sensor', temp_val, convert_to_celcius(temp_val))
   file.write("{}, {}, {}, {}, {}\n".format(
      time.time(),
      convert_to_celcius(builtin_sensor.read_u16()),
      thermistor_sensor.read_u16(),
      humiture_sensor.read_u16(),
      temp_val)
   )
   file.flush()
   time.sleep(delay)
