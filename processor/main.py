import re
import pandas as pd
import numpy as np
from datetime import datetime

from core.Enums import MissValueStrategy
from processor.PreProcessor import PreProcessor

if __name__ == '__main__':
    print("Reading Document ...")
    dataArr = pd.read_csv("../files/raw/online store customer.csv")
    processor = PreProcessor(dataArr)
    processor.changeColumnNames([("Gender", "Sex")])
    processor.changeDataTypes([("Transaction_date", "datetime64[ns]")])
    processor.fillMissValues(
        [("Sex", MissValueStrategy.MODE), ("Amount_spent", MissValueStrategy.MEAN),
         ("Employees_status", MissValueStrategy.MODE), ("Age", MissValueStrategy.MEDIAN)])
    dataArr.info()
