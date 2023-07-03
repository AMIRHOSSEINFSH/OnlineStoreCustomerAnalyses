import numpy as np
import pandas as pd

from core.Enums import MissValueStrategy


class PreProcessor:

    def __init__(self, dataframe):
        self.dataFrame = dataframe

    def changeColumnNames(self, newColumnNames):
        # Create a dictionary with current and new column names
        column_mapping = {current_name: new_name for current_name, new_name in newColumnNames}
        self.dataFrame.rename(columns=column_mapping, inplace=True)

    def changeDataTypes(self, newTypes):
        for pair in newTypes:
            column_name = pair[0]
            new_data_type = pair[1]
            self.dataFrame[column_name] = self.dataFrame[column_name].astype(new_data_type)

    def removeDuplicates(self):
        self.dataFrame.drop_duplicates(keep='first', inplace=True)

    def dropNanRows(self, columns):
        self.dataFrame.dropna(subset=columns, inplace=True)

    def fillMissValues(self, columnsWithStrategy):
        for itPair in columnsWithStrategy:
            strategy = itPair[1]
            if strategy == MissValueStrategy.MODE:
                self.dataFrame[itPair[0]].fillna(self.dataFrame[itPair[0]].mode().iloc[0],
                                                 inplace=True)
            elif strategy == MissValueStrategy.MEAN:
                self.dataFrame[itPair[0]].fillna(self.dataFrame[itPair[0]].mean(), inplace=True)
            elif strategy == MissValueStrategy.MEDIAN:
                self.dataFrame[itPair[0]].fillna(self.dataFrame[itPair[0]].median(), inplace=True)

    def categorizeNumbericValueOf(self, columnName, new_name_column, bins, labels):
        self.dataFrame[new_name_column] = pd.cut(self.dataFrame[columnName], bins=bins, labels=labels)
