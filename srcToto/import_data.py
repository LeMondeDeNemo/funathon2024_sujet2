import pandas as pd
import geopandas as gpd
from .clean_data_frame import clean_dataframe
from .create_data_list import create_data_list

def import_airport_data(list_files):
    # Define the data types for each column
    col_types = {
        "ANMOIS": "str",
        "APT": "str",     # equivalent to col_character()
        "APT_NOM": "str", # equivalent to col_character()
        "APT_ZON": "str", # equivalent to col_character()
    }

    # Read the CSV file(s) with the specified column types
    pax_apt_all = pd.concat([
        pd.read_csv(file, delimiter = ';', dtype = col_types)
        for file in list_files
        ])

    # Clean the DataFrame (assuming clean_dataframe is a predefined function)
    pax_apt_all = clean_dataframe(pax_apt_all)

    return pax_apt_all

def import_compagnies_data(list_files):
    col_type = {
    "ANMOIS": "str",  
    "CIE": "str",
    "CIE_NOM": "str",
    "CIE_NAT": "str", 
    "CIE_PAYS": "str",
    }

    for file in list_files:
        pax_cie_file = pd.concat([pd.read_csv(file, delimiter = ";", dtype = col_type)])
    
    pax_cie_file = clean_dataframe(pax_cie_file)

    return pax_cie_file

def import_liaisons_data(list_files):
    col_type = {
    "ANMOIS": "str",  
    "LSN": "str",
    "LSN_DEP_NOM": "str", 
    "LSN_ARR_NOM": "str",
    "LSN_SCT": "str",
    "LSN_FSC": "str"
    }

    for file in list_files:
        pax_lsn_file = pd.concat([pd.read_csv(file, delimiter = ";", dtype = col_type)])
    
    pax_lsn_file = clean_dataframe(pax_lsn_file)

    return pax_lsn_file


urls = create_data_list("sources.yml")

airports_location = gpd.read_file(urls['geojson']['airport'])
print(airports_location)





