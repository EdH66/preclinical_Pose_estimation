# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 12:38:35 2020

@author: Daniel
"""
import math
import numpy as np
import os
import glob


# %%-----------------------------------------------------------------------------------------------------------
                                                # Set Paths
#-----------------------------------------------------------------------------------------------------------
def CreateDestinationFolder(Source_Path = None, Source_Name = None, Destination_Name = None, Destination_Path = None):  
    """ 
    Creates folder with path similar to Source_Path, where Source_Name is replaced by Destination_Name
    
    Args:
        Source_Path: str
        Path where the source files are located
        e.g. c:\\MouseName\\ExpDate\\Raw\\RecordingName
        
        Source_Name: str
        Label of parent folder containing the recordings
        e.g. 'Raw'
        
        DestinationName: str
        Label of target parent folder
        Replaces in Source_Path, Source_Name with DestinationName
        e.g. 'Aligned'
        
    Returns:
        Destination_Path: str
        Path to the destination folder
        
    """
    
    if Destination_Path == None:
        Destination_Path = Source_Path.replace(Source_Name, Destination_Name)
    
    # Create desination folder
    try: 
        os.makedirs(Destination_Path)
        print('The folder: %s has been created!' % Destination_Path)
    except OSError:
        print('The folder: %s already exists!' % Destination_Path)
        
    if Destination_Path == Source_Path:
        raise NameError('The output path is the same as the input path')
        
    return Destination_Path

    


# %%--------------------------------------------------------------------------------------------
#                       Get list of all files with extension in directory
#-----------------------------------------------------------------------------------------------------------    
def GetFilePaths(Folder, Extension): 
    """ Returns a list of strings representing the paths of all files present in Folder with the Extension specified
    
    Args:
        Folder: str or list of string
        The path of the Folder to look
        
        Extension: str
        '.tif' or '.mmap'
        use "*" to list all file in directory 
        
    Returns:
        fname: list of strings representing the paths of all files present in Folder with the Extension specified
        
    """
    #
    # Print warning for old code
    if Extension=="tif":
        print("Warning! Please use .tif for the future")
        Extension=".tif"
    
    elif Extension=="mmap":
        print("Warning! Please use .mmap for the future")
        Extension=".mmap"
            
    
    
    fname=[]
    if isinstance(Folder, list):
        
        for folder in Folder:
            for file in glob.glob(os.path.join(folder,'*%s' % Extension)):
                fname.append(os.path.abspath(file))

    else:
        for file in glob.glob(os.path.join(Folder,'*%s' % Extension)):
                fname.append(os.path.abspath(file))
    
    fname.sort()    
    
    return fname


# %%--------------------------------------------------------------------------------------------
#                       Print factor of a number
#-----------------------------------------------------------------------------------------------
# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
    

        
# %%--------------------------------------------------------------------------------------------
#                       Get recording name
#-----------------------------------------------------------------------------------------------
def GetRecordingName(Tif_Dir): 
    """ Reads the name of the tif file of the recording
    
    Args:
        Tif_Dir: str
        Path to a folder containing recording tif
        
                        
    Returns:
        RecordingName: str
        
    """    
    
    Tif_FileName = os.path.split(GetFilePaths(Tif_Dir,'.tif')[0])[-1]
    if Tif_FileName.find('_')>0:
        RecordingName = Tif_FileName[:Tif_FileName.find('_')]
    else:
        RecordingName = Tif_FileName[:Tif_FileName.find('.tif')]
    
    return RecordingName


    #%%
def round_half_up(n, decimals=0):
    # until .5 round to floor, above .5 rounds to ceil
    
    multiplier = 10 ** decimals
    return math.floor(n*multiplier + 0.5) / multiplier


def Round_Neg2Floor_Pos2Ceil(Input):
    # Check if input is array
    
    if np.isscalar(Input):
        if Input < 0:
            return np.floor(Input)
            
        if Input >= 0:
            return np.ceil(Input)
        
    else:
        count = 0
        for n in Input:
            if n < 0:
                Input[count] = np.floor(n)
            
            if n >= 0:
                Input[count] = np.ceil(n)
            
            count += 1
        
        return Input
    

