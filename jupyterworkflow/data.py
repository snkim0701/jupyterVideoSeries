
import os
from urllib.request import urlretrieve
import pandas as pd


Fremont_URL='https://data.seattle.gov/api/views/mdbt-9ykn/rows.csv?accessType=DOWNLOAD'
def get_fremont_data(filename='Fremont.csv', url=Fremont_URL,
                     force_download=False):
    """Download and cache the fremont data

    Parameters
    -----
    filename :string(optinal)
      location to save the data
    url: string(optional)
      web location of data
    force_download:bool(optional)
      if True, force redownload of data
    Returns
    ----
    data : pandas.DataFrame
      The fremont bbridge data
    """
    
    if force_download or not os.path.exists(filename):
        urlretrieve(url,filename)
    data = pd.read_csv('fremont.csv',index_col='Date')
    try:
        data.index = pd.to_datetime(data.index, format = '%m/%d/%Y %H:%M:%S %p')
    except TypeError:
        data.index = pd.to_datetime(data.index)      
        
    data.columns =['West', 'East']
    data['Total']=data['East']+data['West']
   
    return data
