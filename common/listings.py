import pandas as pd

# Define the listings data
listings_data = [
    # Similar listings in neighborhood (0,0)
    {
        "offering_type": "sale",
        "n_beds": 3,
        "n_baths": 2,
        "price": 350000,
        "latitude": 0,
        "longitude": 0,
        "property_type": "single_family",
        "area": 1800
    },
    {
        "offering_type": "sale",
        "n_beds": 3,
        "n_baths": 2.5,
        "price": 375000,
        "latitude": 0,
        "longitude": 0,
        "property_type": "single_family",
        "area": 2000
    },
    
    # Similar listings in neighborhood (1,2)
    {
        "offering_type": "rent",
        "n_beds": 2,
        "n_baths": 1,
        "price": 1800,
        "latitude": 1,
        "longitude": 2,
        "property_type": "apartment",
        "area": 950
    },
    {
        "offering_type": "rent",
        "n_beds": 1,
        "n_baths": 1,
        "price": 1500,
        "latitude": 1,
        "longitude": 2,
        "property_type": "apartment",
        "area": 750
    },
    
    # Diverse listings in different neighborhoods
    {
        "offering_type": "sale",
        "n_beds": 5,
        "n_baths": 3.5,
        "price": 750000,
        "latitude": 2,
        "longitude": 3,
        "property_type": "luxury",
        "area": 3500
    },
    {
        "offering_type": "rent",
        "n_beds": 0,
        "n_baths": 1,
        "price": 1200,
        "latitude": 3,
        "longitude": 1,
        "property_type": "studio",
        "area": 500
    },
    {
        "offering_type": "sale",
        "n_beds": 4,
        "n_baths": 2,
        "price": 425000,
        "latitude": 2,
        "longitude": 1,
        "property_type": "townhouse",
        "area": 2200
    },
    {
        "offering_type": "rent",
        "n_beds": 3,
        "n_baths": 2,
        "price": 2500,
        "latitude": 3,
        "longitude": 3,
        "property_type": "condo",
        "area": 1600
    }
]

# Create DataFrame
listings_df = pd.DataFrame(listings_data)

# Encode categorical columns
listings_df = pd.get_dummies(listings_df, columns=["offering_type", "property_type"])

# Create a map that maps a column name to the columns index in the dataset
# This will be used to map column names to vector components
column_name_to_index = dict(map(lambda i: (i[1], i[0]), enumerate(listings_df.columns)))