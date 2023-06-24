# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 21:07:51 2023

@author: Teklehaimanot
"""

# This is my first class to read and clean data 


import pandas as pd
import numpy as np 
import os 

class DataClean(object):  #Why we do it here, I will make t his clear in the following days.
    
    def __init__(self, path, filename, seperator, header = 0):
        
        self.path = path
        self.filename = filename
        self.seperator = seperator
        self.header = header
    
    def read_data(self):
        
        with open(self.filename, "r") as filein:
        
            self.df = pd.read_csv(filein, sep = self.seperator, header = self.header)
            
            # self help us to attach every method and attributes to the class DataClean
            
        return self # 
            
            # for line in data_as_lines:
                
                # line_as_list = line.strip().split()
                
                # var1_list.append(line_as_list[0])
                # var2_list.append(line_as_list[1])
                # var3_list.append(line_as_list[2])
                # var4_list.append(line_as_list[3])
        
            # df = pd.read_csv(filein, self.sep)
            
            # return df 
            
           
    def drop_columns(self, columns_to_drop_list):
    
         
    
        self.df = self.read_data(self).drop(columns = columns_to_drop_list, axis = 1)
        
      
        return self
    
    def convert_datatype(self, datetime_format):
    
    
        self.df = self.drop_columns(self)
        
        for index, col in enumerate(self.df.columns):
            
            if index ==0: # Assuming my data is all float and the first column is date time so 
            
               self.df.iloc[:,0] = pd.to_datetime(self.df.iloc[:,0], format = datetime_format)
                
            
            else:
                self.df[col] = self.df[col].astype(float)
                
        return self       