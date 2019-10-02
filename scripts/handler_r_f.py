"""handler_geo"""

import rasterio
import fiona
import pandas as pd
import pymongo
import requests
import numpy

def handler(event, context):
    """
    Handle bounds requests
    """
    print(event, context)

    return True
