'''takes in a file name and returns values
in a column that match a query_value'''

import sys


def get_column(file_name = '', query_column = 0, query_value = '', result_column=3):
    '''Returns a list of values from the query inputs
    Parameters
    ----------

    file_name: string
               name of file to access
    query_column: int
                  column to perform query on
    query_value: int
                 which country to perform search on
    resut_column: int
                  the column that has value of interest
    '''
    matchingValues = []

    try:
        with open('../data/'+file_name, 'r') as f:

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
    except ValueError:
        print('Error in converting query column to an integer')
        sys.exit(1)

    return matchingValues

def get_mean(array = []):
    '''Returns the mean of a list of values from the list of values
    Parameters
    ----------
    array: list
           list of integers on which to compute mean
    '''
    
    return sum(array)/len(array)

def get_median(array = []):
    '''Returns the median of a list of values from the list of values
    Parameters
    ----------
    array: list
           list of integers on which to compute median
    '''
    sorted_array = sorted(array)
    length = len(sorted_list)
    
    if length % 2 == 1:
        return sorted_list[length // 2]
    
    else:
        middle1 = sorted_list[(length // 2) - 1]
        middle2 = sorted_list[length // 2]
        return (middle1 + middle2) / 2
