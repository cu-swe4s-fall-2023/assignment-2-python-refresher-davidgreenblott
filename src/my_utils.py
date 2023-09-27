'''takes in a file name and returns values
in a column that match a query_value'''

import sys


def get_column(file_name, query_column, query_value, result_column=1):
    '''Returns a list of values from the query inputs
    Parameters
    ----------

    file_name: string
               name of file to access
    query_column: int
                  column to perform query on
    query_value: int
                 which country to perform wserach on
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
