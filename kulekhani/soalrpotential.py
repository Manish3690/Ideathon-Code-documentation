import pandas as pd
import pvlib
from pvlib import location
from pvlib import irradiance
import datetime

# Load weather data from CSV
weather = pd.read_csv('your_file.csv')
weather.index = pd.date_range(start='2019-01-01', end='2024-12-31', freq='H')

# Specify constants
latitude, longitude, tz = 27.6018, 85.1587, 'Asia/Kathmandu'
surface_tilt = 19
surface_azimuth = 0  # PV facing north

# Create location object
site = location.Location(latitude, longitude, tz=tz)

# Calculate solar position
solpos = site.get_solarposition(weather.index)

# Calculate POA irradiance
poa_irradiance = irradiance.get_total_irradiance(
    surface_tilt,
    surface_azimuth,
    solpos['apparent_zenith'],
    solpos['azimuth'],
    weather['DNI'],
    weather['GHI'],
    weather['DHI'],
    model='liujordan'
)

# The DataFrame 'poa_irradiance' now contains the POA irradiance data
print(poa_irradiance)

