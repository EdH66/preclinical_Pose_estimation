# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 13:45:29 2021

@author: Daniel
"""
import numpy as np


#%%
def MedianFilterPos(PointPos, SizeFilt=2):
    """
    Performs median filtering of coordinates.

    PointPos_Median = MedianFilterPos(PointPos, SizeFilt=2)

    
    Parameters
    ----------
    PointPos : TYPE 2d array of float64 (ntimepoints x ncoordinates)
        DESCRIPTION.
        
    SizeFilt : int
    Half size of filter

    Returns
    -------
    PointPos_Median.

    """
    nTimepoints = PointPos.shape[0]
    
    
    if len(PointPos.shape) == 1:
        PointPos = np.expand_dims(PointPos, axis = 1)
    
    PointPos_Median = np.empty_like(PointPos)
    for timepoint in range(SizeFilt, nTimepoints-SizeFilt):
        PointPos_Median[timepoint, :] = np.median(PointPos[timepoint-SizeFilt:timepoint+SizeFilt+1, :], axis=0)
        
    for timepoint in range(SizeFilt):
        PointPos_Median[timepoint, :] = np.median(PointPos[:timepoint+SizeFilt+1, :], axis=0)
    for timepoint in range(nTimepoints-SizeFilt, nTimepoints):
        PointPos_Median[timepoint, :] = np.median(PointPos[timepoint:, :], axis=0)    
        
    return PointPos_Median