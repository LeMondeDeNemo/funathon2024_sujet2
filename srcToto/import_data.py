import pandas as pd
import geopandas as gpd
from clean_data_frame import clean_dataframe

def import_airport_data(list_files):
    col_type = {
    "ANMOIS": "str",  
    "APT": "str",
    "APT_NOM": "str", 
    "APT_ZON": "str",
    }

    for file in list_files:
        pax_apt_file = pd.concat([pd.read_csv(file, delimiter = ";", dtype = col_type)])
    
    pax_apt_file = clean_dataframe(pax_apt_file)

    return pax_apt_file

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

from create_data_list import create_data_list

urls = create_data_list("sources.yml")

airports_location = gpd.read_file(urls['geojson']['airport'])
print(airports_location)
