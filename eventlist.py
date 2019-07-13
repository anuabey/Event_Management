# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:38:11 2018
This program uses the pandas dataframe to read from a CSV file 
containing event and participant details, sort the values 
event-wise & writes the data to multiple CSV files based 
on the event 
@author: Anu Mary Abey
"""

import pandas as pd
def main():
    """Reads the CSV file, recategorizes the data & 
    writes to different CSV files based on each event """
    individual = pd.read_csv("individual_1.csv")
    event = individual.Event.unique()
    [individual[individual['Event'] == i ].to_csv(i+".csv") for i in event]

if __name__ == "__main__":
        main()