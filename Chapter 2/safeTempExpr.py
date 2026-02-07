print('Enter C or F to indicate Celsius or Fahrenheit:')
temp_unit = input()
print('Enter the number of degrees:')
degrees = int(input())
if (temp_unit == 'C' and (degrees >= 16 and degrees <= 38)) or (temp_unit == 'F' and (degrees >= 60.8 and degrees <= 100.4)):
    print('Safe')
else:
    print('Dangerous')