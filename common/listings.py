import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

listings_data = [
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2500,
    "latitude": 0,
    "longitude": 0,
    "property_type": "condo",
    "area": 1600
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1800,
    "latitude": 0,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1050
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 450000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "house",
    "area": 2200
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1400,
    "latitude": 0,
    "longitude": 0,
    "property_type": "studio",
    "area": 750
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 325000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2100,
    "latitude": 0,
    "longitude": 1,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 3,
    "price": 520000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "house",
    "area": 2600
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1350,
    "latitude": 0,
    "longitude": 1,
    "property_type": "apartment",
    "area": 800
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 298000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1600
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3200,
    "latitude": 0,
    "longitude": 1,
    "property_type": "house",
    "area": 2100
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 275000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2400,
    "latitude": 0,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1450
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 480000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1750,
    "latitude": 0,
    "longitude": 2,
    "property_type": "apartment",
    "area": 950
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 310000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1700
  },
  {
    "offering_type": "rent",
    "n_beds": 5,
    "n_baths": 3,
    "price": 3600,
    "latitude": 0,
    "longitude": 3,
    "property_type": "house",
    "area": 2800
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 340000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "condo",
    "area": 1500
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1500,
    "latitude": 0,
    "longitude": 3,
    "property_type": "apartment",
    "area": 780
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 495000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "house",
    "area": 2350
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2200,
    "latitude": 0,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1350
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 378000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 1950
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1900,
    "latitude": 1,
    "longitude": 0,
    "property_type": "condo",
    "area": 1100
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 225000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "apartment",
    "area": 850
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2600,
    "latitude": 1,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1550
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 425000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 2250
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2300,
    "latitude": 1,
    "longitude": 1,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 360000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1800
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1450,
    "latitude": 1,
    "longitude": 1,
    "property_type": "apartment",
    "area": 820
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 550000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "house",
    "area": 2700
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2700,
    "latitude": 1,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1650
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 290000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2550,
    "latitude": 1,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1500
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 460000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "house",
    "area": 2400
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1850,
    "latitude": 1,
    "longitude": 2,
    "property_type": "apartment",
    "area": 980
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 320000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3100,
    "latitude": 1,
    "longitude": 3,
    "property_type": "house",
    "area": 2200
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 285000,
    "latitude": 1,
    "longitude": 3,
    "property_type": "condo",
    "area": 1350
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1550,
    "latitude": 1,
    "longitude": 3,
    "property_type": "apartment",
    "area": 800
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 405000,
    "latitude": 1,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1900
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2150,
    "latitude": 1,
    "longitude": 3,
    "property_type": "condo",
    "area": 1200
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 370000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "house",
    "area": 1900
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1950,
    "latitude": 2,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1100
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 230000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "condo",
    "area": 900
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2750,
    "latitude": 2,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1600
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 440000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2050,
    "latitude": 2,
    "longitude": 1,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 355000,
    "latitude": 2,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1700
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1350,
    "latitude": 2,
    "longitude": 1,
    "property_type": "studio",
    "area": 650
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 580000,
    "latitude": 2,
    "longitude": 1,
    "property_type": "house",
    "area": 2800
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2500,
    "latitude": 2,
    "longitude": 1,
    "property_type": "apartment",
    "area": 1500
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 300000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2650,
    "latitude": 2,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1650
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 475000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "house",
    "area": 2450
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1800,
    "latitude": 2,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1000
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 335000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3300,
    "latitude": 2,
    "longitude": 3,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 295000,
    "latitude": 2,
    "longitude": 3,
    "property_type": "condo",
    "area": 1400
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1650,
    "latitude": 2,
    "longitude": 3,
    "property_type": "apartment",
    "area": 850
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 420000,
    "latitude": 2,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1950
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2250,
    "latitude": 2,
    "longitude": 3,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 395000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "house",
    "area": 2100
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 2100,
    "latitude": 3,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1150
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 245000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "condo",
    "area": 950
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2850,
    "latitude": 3,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1700
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 465000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "house",
    "area": 2400
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2200,
    "latitude": 3,
    "longitude": 1,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 380000,
    "latitude": 3,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1850
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1550,
    "latitude": 3,
    "longitude": 1,
    "property_type": "apartment",
    "area": 800
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 610000,
    "latitude": 3,
    "longitude": 1,
    "property_type": "house",
    "area": 2900
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2700,
    "latitude": 3,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1600
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 320000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "condo",
    "area": 1350
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2800,
    "latitude": 3,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1550
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 490000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "house",
    "area": 2500
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1950,
    "latitude": 3,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1050
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 350000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1800
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3500,
    "latitude": 3,
    "longitude": 3,
    "property_type": "house",
    "area": 2400
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 315000,
    "latitude": 3,
    "longitude": 3,
    "property_type": "condo",
    "area": 1450
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1750,
    "latitude": 3,
    "longitude": 3,
    "property_type": "apartment",
    "area": 900
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 435000,
    "latitude": 3,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 2000
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2350,
    "latitude": 3,
    "longitude": 3,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2500,
    "latitude": 0,
    "longitude": 0,
    "property_type": "condo",
    "area": 1600
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1800,
    "latitude": 0,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1050
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 450000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "house",
    "area": 2200
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1400,
    "latitude": 0,
    "longitude": 0,
    "property_type": "studio",
    "area": 750
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 325000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2100,
    "latitude": 0,
    "longitude": 1,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 3,
    "price": 520000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "house",
    "area": 2600
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1350,
    "latitude": 0,
    "longitude": 1,
    "property_type": "apartment",
    "area": 800
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 298000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1600
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3200,
    "latitude": 0,
    "longitude": 1,
    "property_type": "house",
    "area": 2100
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 275000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2400,
    "latitude": 0,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1450
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 480000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1750,
    "latitude": 0,
    "longitude": 2,
    "property_type": "apartment",
    "area": 950
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 310000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1700
  },
  {
    "offering_type": "rent",
    "n_beds": 5,
    "n_baths": 3,
    "price": 3600,
    "latitude": 0,
    "longitude": 3,
    "property_type": "house",
    "area": 2800
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 340000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "condo",
    "area": 1500
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1500,
    "latitude": 0,
    "longitude": 3,
    "property_type": "apartment",
    "area": 780
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 495000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "house",
    "area": 2350
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2200,
    "latitude": 0,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1350
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 378000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 1950
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1900,
    "latitude": 1,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1100
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 225000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "apartment",
    "area": 850
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2600,
    "latitude": 1,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1550
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 425000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 2250
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2300,
    "latitude": 1,
    "longitude": 1,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 360000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1800
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1450,
    "latitude": 1,
    "longitude": 1,
    "property_type": "apartment",
    "area": 820
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 550000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "house",
    "area": 2700
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2700,
    "latitude": 1,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1650
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 290000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2550,
    "latitude": 1,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1500
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 460000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "house",
    "area": 2400
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1850,
    "latitude": 1,
    "longitude": 2,
    "property_type": "apartment",
    "area": 980
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 320000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3100,
    "latitude": 1,
    "longitude": 3,
    "property_type": "house",
    "area": 2200
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 285000,
    "latitude": 1,
    "longitude": 3,
    "property_type": "condo",
    "area": 1350
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1550,
    "latitude": 1,
    "longitude": 3,
    "property_type": "apartment",
    "area": 800
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 405000,
    "latitude": 1,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1900
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2150,
    "latitude": 1,
    "longitude": 3,
    "property_type": "condo",
    "area": 1200
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 370000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "house",
    "area": 1900
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1950,
    "latitude": 2,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1100
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 230000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "condo",
    "area": 900
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2750,
    "latitude": 2,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1600
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 440000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2050,
    "latitude": 2,
    "longitude": 1,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 355000,
    "latitude": 2,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1700
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1350,
    "latitude": 2,
    "longitude": 1,
    "property_type": "studio",
    "area": 650
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 580000,
    "latitude": 2,
    "longitude": 1,
    "property_type": "house",
    "area": 2800
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2500,
    "latitude": 2,
    "longitude": 1,
    "property_type": "apartment",
    "area": 1500
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 300000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2650,
    "latitude": 2,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1650
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 475000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "house",
    "area": 2450
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1800,
    "latitude": 2,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1000
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 335000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3300,
    "latitude": 2,
    "longitude": 3,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 295000,
    "latitude": 2,
    "longitude": 3,
    "property_type": "condo",
    "area": 1400
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1650,
    "latitude": 2,
    "longitude": 3,
    "property_type": "apartment",
    "area": 850
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 420000,
    "latitude": 2,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1950
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2250,
    "latitude": 2,
    "longitude": 3,
    "property_type": "condo",
    "area": 1250
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 395000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "house",
    "area": 2100
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 2100,
    "latitude": 3,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1150
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 245000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "condo",
    "area": 950
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2850,
    "latitude": 3,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1700
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 465000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "house",
    "area": 2400
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2200,
    "latitude": 3,
    "longitude": 1,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 380000,
    "latitude": 3,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1850
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1550,
    "latitude": 3,
    "longitude": 1,
    "property_type": "apartment",
    "area": 800
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 610000,
    "latitude": 3,
    "longitude": 1,
    "property_type": "house",
    "area": 2900
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2700,
    "latitude": 3,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1600
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 320000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "condo",
    "area": 1350
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2800,
    "latitude": 3,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1550
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 490000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "house",
    "area": 2500
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1950,
    "latitude": 3,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1050
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 350000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1800
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3500,
    "latitude": 3,
    "longitude": 3,
    "property_type": "house",
    "area": 2400
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 315000,
    "latitude": 3,
    "longitude": 3,
    "property_type": "condo",
    "area": 1450
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1750,
    "latitude": 3,
    "longitude": 3,
    "property_type": "apartment",
    "area": 900
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 435000,
    "latitude": 3,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 2000
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2350,
    "latitude": 3,
    "longitude": 3,
    "property_type": "condo",
    "area": 1300
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 365000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "house",
    "area": 1850
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1850,
    "latitude": 0,
    "longitude": 0,
    "property_type": "condo",
    "area": 1100
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 240000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "apartment",
    "area": 780
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2650,
    "latitude": 0,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1700
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 498000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "house",
    "area": 2400
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2250,
    "latitude": 0,
    "longitude": 1,
    "property_type": "condo",
    "area": 1350
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 352000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1720
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1500,
    "latitude": 0,
    "longitude": 1,
    "property_type": "apartment",
    "area": 850
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 585000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "house",
    "area": 2750
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2800,
    "latitude": 0,
    "longitude": 1,
    "property_type": "house",
    "area": 1650
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 289000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "condo",
    "area": 1280
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2450,
    "latitude": 0,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1600
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 462000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "house",
    "area": 2350
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1780,
    "latitude": 0,
    "longitude": 2,
    "property_type": "apartment",
    "area": 920
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 325000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3400,
    "latitude": 0,
    "longitude": 3,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 298000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "condo",
    "area": 1400
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1600,
    "latitude": 0,
    "longitude": 3,
    "property_type": "apartment",
    "area": 820
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 415000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1950
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2280,
    "latitude": 0,
    "longitude": 3,
    "property_type": "condo",
    "area": 1320
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 389000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 1900
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 389000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 2050
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1920,
    "latitude": 1,
    "longitude": 0,
    "property_type": "condo",
    "area": 1150
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 235000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "apartment",
    "area": 820
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2680,
    "latitude": 1,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1580
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 445000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 2350
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2350,
    "latitude": 1,
    "longitude": 1,
    "property_type": "condo",
    "area": 1320
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 372000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1850
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1480,
    "latitude": 1,
    "longitude": 1,
    "property_type": "studio",
    "area": 700
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 565000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "house",
    "area": 2750
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2750,
    "latitude": 1,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1680
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 302000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "condo",
    "area": 1280
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2580,
    "latitude": 1,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1520
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 472000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "house",
    "area": 2450
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1890,
    "latitude": 1,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1000
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 335000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1780
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3200,
    "latitude": 1,
    "longitude": 3,
    "property_type": "house",
    "area": 2250
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 292000,
    "latitude": 1,
    "longitude": 3,
    "property_type": "condo",
    "area": 1380
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1580,
    "latitude": 1,
    "longitude": 3,
    "property_type": "apartment",
    "area": 820
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 412000,
    "latitude": 1,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1920
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2180,
    "latitude": 1,
    "longitude": 3,
    "property_type": "condo",
    "area": 1220
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 380000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "house",
    "area": 1950
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1980,
    "latitude": 2,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1120
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 238000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "condo",
    "area": 920
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2780,
    "latitude": 2,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1630
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 452000,
    "latitude": 2,
    "longitude": 0,
    "property_type": "house",
    "area": 2350
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2080,
    "latitude": 2,
    "longitude": 1,
    "property_type": "condo",
    "area": 1270
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 362000,
    "latitude": 2,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1720
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1380,
    "latitude": 2,
    "longitude": 1,
    "property_type": "studio",
    "area": 670
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 595000,
    "latitude": 2,
    "longitude": 1,
    "property_type": "house",
    "area": 2850
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2550,
    "latitude": 2,
    "longitude": 1,
    "property_type": "apartment",
    "area": 1550
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 308000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "condo",
    "area": 1320
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2680,
    "latitude": 2,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1680
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 482000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "house",
    "area": 2480
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1830,
    "latitude": 2,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1020
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 342000,
    "latitude": 2,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1780
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3350,
    "latitude": 2,
    "longitude": 3,
    "property_type": "house",
    "area": 2350
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 302000,
    "latitude": 2,
    "longitude": 3,
    "property_type": "condo",
    "area": 1430
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1680,
    "latitude": 2,
    "longitude": 3,
    "property_type": "apartment",
    "area": 870
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 428000,
    "latitude": 2,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1980
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2280,
    "latitude": 2,
    "longitude": 3,
    "property_type": "condo",
    "area": 1280
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 405000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "house",
    "area": 2150
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 2150,
    "latitude": 3,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1180
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 252000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "condo",
    "area": 970
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2880,
    "latitude": 3,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1720
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 472000,
    "latitude": 3,
    "longitude": 0,
    "property_type": "house",
    "area": 2450
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2250,
    "latitude": 3,
    "longitude": 1,
    "property_type": "condo",
    "area": 1320
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 388000,
    "latitude": 3,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1880
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1580,
    "latitude": 3,
    "longitude": 1,
    "property_type": "apartment",
    "area": 820
  },
  {
    "offering_type": "sale",
    "n_beds": 5,
    "n_baths": 4,
    "price": 625000,
    "latitude": 3,
    "longitude": 1,
    "property_type": "house",
    "area": 2950
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2750,
    "latitude": 3,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1650
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 328000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "condo",
    "area": 1380
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2850,
    "latitude": 3,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1580
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 498000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "house",
    "area": 2550
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1980,
    "latitude": 3,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1080
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 358000,
    "latitude": 3,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1820
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3550,
    "latitude": 3,
    "longitude": 3,
    "property_type": "house",
    "area": 2450
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 322000,
    "latitude": 3,
    "longitude": 3,
    "property_type": "condo",
    "area": 1480
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1780,
    "latitude": 3,
    "longitude": 3,
    "property_type": "apartment",
    "area": 920
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 3,
    "price": 442000,
    "latitude": 3,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 2050
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 2,
    "price": 2380,
    "latitude": 3,
    "longitude": 3,
    "property_type": "condo",
    "area": 1350
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 345000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1720
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1820,
    "latitude": 0,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1020
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 232000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "studio",
    "area": 700
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3250,
    "latitude": 0,
    "longitude": 0,
    "property_type": "house",
    "area": 2300
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 295000,
    "latitude": 0,
    "longitude": 0,
    "property_type": "condo",
    "area": 1400
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2620,
    "latitude": 0,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1650
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 465000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "house",
    "area": 2450
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1420,
    "latitude": 0,
    "longitude": 1,
    "property_type": "studio",
    "area": 680
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 285000,
    "latitude": 0,
    "longitude": 1,
    "property_type": "condo",
    "area": 1350
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2750,
    "latitude": 0,
    "longitude": 1,
    "property_type": "apartment",
    "area": 1550
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 342000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1780
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1880,
    "latitude": 0,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1080
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 245000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "condo",
    "area": 950
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3350,
    "latitude": 0,
    "longitude": 2,
    "property_type": "house",
    "area": 2350
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 305000,
    "latitude": 0,
    "longitude": 2,
    "property_type": "condo",
    "area": 1420
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2850,
    "latitude": 0,
    "longitude": 3,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 485000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "house",
    "area": 2500
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1620,
    "latitude": 0,
    "longitude": 3,
    "property_type": "studio",
    "area": 720
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 295000,
    "latitude": 0,
    "longitude": 3,
    "property_type": "condo",
    "area": 1380
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2780,
    "latitude": 0,
    "longitude": 3,
    "property_type": "apartment",
    "area": 1580
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 352000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "townhouse",
    "area": 1750
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1950,
    "latitude": 1,
    "longitude": 0,
    "property_type": "apartment",
    "area": 1050
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 232000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "studio",
    "area": 680
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3280,
    "latitude": 1,
    "longitude": 0,
    "property_type": "house",
    "area": 2280
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 312000,
    "latitude": 1,
    "longitude": 0,
    "property_type": "condo",
    "area": 1450
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2680,
    "latitude": 1,
    "longitude": 1,
    "property_type": "townhouse",
    "area": 1680
  },
  {
    "offering_type": "sale",
    "n_beds": 4,
    "n_baths": 3,
    "price": 475000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "house",
    "area": 2480
  },
  {
    "offering_type": "rent",
    "n_beds": 1,
    "n_baths": 1,
    "price": 1480,
    "latitude": 1,
    "longitude": 1,
    "property_type": "apartment",
    "area": 750
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 298000,
    "latitude": 1,
    "longitude": 1,
    "property_type": "condo",
    "area": 1380
  },
  {
    "offering_type": "rent",
    "n_beds": 3,
    "n_baths": 2,
    "price": 2720,
    "latitude": 1,
    "longitude": 1,
    "property_type": "apartment",
    "area": 1520
  },
  {
    "offering_type": "sale",
    "n_beds": 3,
    "n_baths": 2,
    "price": 348000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "townhouse",
    "area": 1820
  },
  {
    "offering_type": "rent",
    "n_beds": 2,
    "n_baths": 1,
    "price": 1880,
    "latitude": 1,
    "longitude": 2,
    "property_type": "apartment",
    "area": 1080
  },
  {
    "offering_type": "sale",
    "n_beds": 1,
    "n_baths": 1,
    "price": 252000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "studio",
    "area": 720
  },
  {
    "offering_type": "rent",
    "n_beds": 4,
    "n_baths": 3,
    "price": 3380,
    "latitude": 1,
    "longitude": 2,
    "property_type": "house",
    "area": 2380
  },
  {
    "offering_type": "sale",
    "n_beds": 2,
    "n_baths": 2,
    "price": 312000,
    "latitude": 1,
    "longitude": 2,
    "property_type": "condo",
    "area": 1420
  }
]

# Create DataFrame
listings_df = pd.DataFrame(listings_data)

# Encode categorical columns
listings_df = pd.get_dummies(listings_df, columns=["offering_type", "property_type"])

# Scale the dataset
scaler = MinMaxScaler()
listings = scaler.fit_transform(listings_df).astype(np.float32)

# Create a map that maps a column name to the columns index in the dataset
# This will be used to map column names to vector components
column_name_to_index = dict(map(lambda i: (i[1], i[0]), enumerate(listings_df.columns)))