# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def time_series():
    """Pytest fixture to create some random data with flatlines"""
    time_series_length = 5000

    test_data = 1000 * np.random.random(time_series_length)

    flatline0 = [375] * 10
    flatline1 = [400] * 200
    flatline2 = [568] * 100
    flatline3 = [400] * 400
    flatline4 = [300] * 300
    flatline5 = [150] * 600
    flatline6 = [730] * 800
    flatline7 = 500 + np.random.random(size=600)/1000
    # flatline8 = [5+x/1000 for x in range(10000)]
    
    test_data = np.insert(test_data, 0, flatline0)
    test_data = np.insert(test_data, 5000, flatline1)
    test_data = np.insert(test_data, 30, flatline2)
    test_data = np.insert(test_data, 998, flatline3)
    test_data = np.insert(test_data, 999, flatline4)
    test_data = np.insert(test_data, 1000, flatline5)
    test_data = np.insert(test_data, 3000, flatline6)
    test_data = np.insert(test_data, 2500, flatline7)
    # test_data = np.insert(test_data, 2700, flatline8)
    
    return test_data



def _filter_time_series_for_flatlines(time_series, maximum_jitter):
    """Filter a time series to only include sections that are flatlines
    Parameters
    ----------
    time_series : numpy.ndarray
        Time series, provided as a numpy array.
    maximum_jitter : float
        maximum allowed deviation from previous point to be considered still
        a flatline
        #TODO
        I've just realised that you could have increasing or decreasing amount
        that is under the maximum jitter and it would get picked up as a flatline 
        Gonna have to figure this one out...
        
    Returns
    -------
    flatlines : pandas.core.frame.DataFrame
        DataFrame containing filtered flatlines
    """
    diff = np.diff(time_series)
    # diff = np.insert(diff, 0, np.NaN)
    
    flatlines = pd.DataFrame()
    
    flatline_index = []
    flatline_value = []
    
    for i, diff_value in enumerate(diff):
        if abs(diff_value) < maximum_jitter:
            value = time_series[i]
            flatline_index.append(i)
            flatline_value.append(value)
    
    flatlines['pos_in_ts'] = flatline_index
    flatlines['flatline_value'] = flatline_value
    flatlines['value_diff'] = flatlines['flatline_value'].diff()
    return flatlines

def _filter_flatlines_for_startpoints(flatlines, maximum_jitter):
    """Finds the flatline startpoints from a time series filtered to only
    include flatlines
    
    Parameters
    ----------
    flatlines : pandas.core.frame.DataFrame
        DataFrame containing filtered flatlines
    maximum_jitter : float
        maximum allowable deviation from previous point
        #TODO change this to a standard devation of a window or something
        
    Returns
    -------
    flatline_starts : pandas.core.frame.DataFrame
        DataFrame containing flatlines startpoints
    """
    flatline_starts = flatlines[abs(flatlines['value_diff']) > maximum_jitter]
    flatline_starts['type'] = 'start'
    return flatline_starts

def _find_flatline_endpoints(flatlines, flatline_starts):
    """Finds the flatline endpoints by locating the rows preceding the start
    points in the filtered flatlines df
    
    Parameters
    ----------
    flatlines : pandas.core.frame.DataFrame
        DataFrame containing filtered flatlines
    flatline_starts : pandas.core.frame.DataFrame
        DataFrame containing flatline startpoints
        
    Returns
    -------
    flatline_ends : pandas.core.frame.DataFrame
        DataFrame containing flatlines endpoints
    """
    flatline_ends = flatlines.iloc[flatline_starts.index-1]
    flatline_ends['pos_in_ts'] += 1
    flatline_ends['type'] = 'end'
    return flatline_ends

def _concat_start_and_endpoints(flatline_starts, flatline_ends):
    """concatinate flatline start and ends 
    
    Parameters
    ----------
    flatlines : pandas.core.frame.DataFrame
        DataFrame containing filtered flatlines
    flatline_starts : pandas.core.frame.DataFrame
        DataFrame containing flatline startpoints
        
    Returns
    -------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
    """
    all_flatlines = pd.concat([flatline_starts, flatline_ends]).set_index('pos_in_ts')
    all_flatlines = all_flatlines.sort_index()
    return all_flatlines

def _check_for_flatlines_at_start(all_flatlines):
    """Check if were flatlines present at the start of the time_series
    if so add them to the DataFrame.
    
    Parameters
    ----------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
        
    Returns
    -------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
    """
    if all_flatlines.head(1)['type'].any() != 'start':
        start = flatlines.head(1).set_index('pos_in_ts')
        start['type'] = 'start'
        all_flatlines = all_flatlines.append(start)
        return all_flatlines
    else:
        return all_flatlines
        
def _check_for_flatlines_at_end(all_flatlines):
    """Check if were flatlines present at the end of the time_series
    if so add them to the DataFrame.
    
    Parameters
    ----------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
        
    Returns
    -------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
    """
    if all_flatlines.tail(1)['type'].any() != 'end':
        end = flatlines.tail(1).set_index('pos_in_ts')
        end.loc[:, 'type'] = 'end'
        all_flatlines = all_flatlines.append(end)  
        return all_flatlines
    else:
        return all_flatlines

def _calclulate_flatline_lengths(all_flatlines):
    """Calculate the length of the found flatlines
    
    Parameters
    ----------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
        
    Returns
    -------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
    """
    all_flatlines['length'] = np.insert(np.diff(all_flatlines.index), 0, 0)
    all_flatlines['length'][::2] = np.NaN
    return all_flatlines

def _split_all_flatlines(all_flatlines):
    """Split up DataFrame of flatlines into the individual components 

    Parameters
    ----------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints

    Returns
    -------
    split_flatlines : list
        list of DataFrames with two rows each corresponding to start and end
    """
    split_flatlines = []
    for i in range(0, len(all_flatlines), 2):
        split_flatlines.append(all_flatlines[i:2+i])
    return split_flatlines

def _filter_short_flatlines(all_flatlines, min_flatline_length):
    """Filter out flatlines under a minimum length
    
    Parameters
    ----------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
    min_flatline_length : float
        minimum length of a flatline

    Returns
    -------
    all_flatlines : pandas.core.frame.DataFrame
        DataFrame containing flatlines start and endpoints
    """
    split_flatlines = _split_all_flatlines(all_flatlines)
    for flatline in split_flatlines:
        if (flatline['length'] < min_flatline_length).any():
            split_flatlines.remove(flatline)
    all_flatlines = pd.concat(split_flatlines)
    return all_flatlines

def _score_flatlines():
    #TODO
    pass

def flatlines_dataframe_to_namedtuple():
    #TODO
    return flatlines

min_flatline_length = 12
maximum_jitter = 1e-3

time_series = time_series()

flatlines = _filter_time_series_for_flatlines(time_series, maximum_jitter)

flatline_starts = _filter_flatlines_for_startpoints(flatlines, maximum_jitter)
flatline_ends = _find_flatline_endpoints(flatlines, flatline_starts)

all_flatlines = _concat_start_and_endpoints(flatline_starts, flatline_ends)
all_flatlines = _check_for_flatlines_at_start(all_flatlines)
all_flatlines = _check_for_flatlines_at_end(all_flatlines)
all_flatlines = all_flatlines.sort_index()
all_flatlines = all_flatlines.drop('value_diff', axis=1)
all_flatlines = _calclulate_flatline_lengths(all_flatlines)
all_flatlines = _filter_short_flatlines(all_flatlines, min_flatline_length)


binsize = int(len(time_series)/min_flatline_length)

print(all_flatlines)
    
plt.plot(time_series)
plt.show()