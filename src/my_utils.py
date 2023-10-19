'''takes in a file name and returns values
in a column that match a query_value'''

import sys
import os

def get_column_from_name(file_name='', column_name = ''):
    '''Returns the index of the column corresponding to the passed in column name
    Parameters
    ----------

    file_name: string
               file path and name of file to access
    column_name: str
                 column search for
    Returns
    -------
    
    column_index: int
                  column index from file
    '''
    try:
        with open(file_name, 'r') as f:

            header = f.readline()
            items = header.strip().split(',')
        
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)
    except TypeError:
        print('Error in converting query column to an integer')
        sys.exit(1)
    
    try:

        return items.index(column_name)
    except ValueError:
        print(f'Value Error: {column_name} not found')
        sys.exit(1)


def get_column(file_name='', query_column=0, query_value='', result_column=3):
    '''Returns a list of values from the query inputs
    Parameters
    ----------

    file_name: string
               file path and name of file to access
    query_column: int
                  column to perform query on
    query_value: int
                 which country to perform search on
    result_column: int
                  the column that has value of interest
    '''
    matchingValues = []

    try:
        with open(file_name, 'r') as f:

            for line in f:

                items = line.strip().split(',')

                if items[query_column] == str(query_value):

                    matchingValues.append(int(float(items[result_column])))

    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)
    except TypeError:
        print('Error in converting query column to an integer')
        sys.exit(1)

    return matchingValues


def get_mean(array=[]):
    '''Returns the mean of a list of values from the list of values
    Parameters
    ----------
    array: list
           list of integers on which to compute mean
    '''

    try:

        return sum(array)/len(array)
    except TypeError:
        print('Error computing mean of array')
        sys.exit(1)


def get_median(array=[]):
    '''Returns the median of a list of values from the list of values
    Parameters
    ----------
    array: list
           list of integers on which to compute median
    '''
    sorted_array = sorted(array)
    length = len(sorted_array)

    if length % 2 == 1:
        return sorted_array[length // 2]

    else:
        middle1 = sorted_array[(length // 2) - 1]
        middle2 = sorted_array[length // 2]
        return (middle1 + middle2) / 2


def get_standard_deviation(array=[]):
    '''Returns the standard deviation of a list of values
    Parameters
    ----------
    array: list
           list of integers on which to compute standard deviation
    '''

    mean = get_mean(array)
    n = len(array)
    sum_squared_diff = sum((x - mean) ** 2 for x in array)
    variance = sum_squared_diff / (n - 1)
    std_deviation = variance ** 0.5

    return std_deviation
