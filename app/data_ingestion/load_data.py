# This module contains the logic for loading the data into Pandas data frame

import pandas as pd
import os
from typing import Optional, List, Dict, Any

class HouseTaxData:
    def __init__(self, file_path: str, ):
        self.file_path = file_path

    def load(self):
        df = pd.read_excel(self.file_path, engine="openpyxl")
        return df
    

htd = HouseTaxData(r"./app/data/Khazipur-DCB.xlsx")
# print(htd.load())



    