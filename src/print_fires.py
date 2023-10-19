'''Prints out the total number of fires for a given country
    * get_user_args() - accepts user input from command line
    * main() - calls get_column() to find query result'''

import my_utils
import argparse
import os


def get_user_args():
    """Accepts user input from command line
    Parameters
    ----------
    Returns
    -------
    parser
    arg parser with country, country_column, fires_column, and file_name fields
    """
    parser = argparse.ArgumentParser(
                description='Add parameters for query search')
    parser.add_argument('--country',
                        type=str,
                        help='The name of the query country',
                        required=True)
    parser.add_argument('--country_column',
                        type=int,
                        help='The index of the column containing countries',
                        required=True)
    parser.add_argument('--result_column',
                        type=int,
                        help='The index of the column containing data of interest',
                        required=True)
    parser.add_argument('--file_name',
                        type=str,
                        help='The file name',
                        required=True)
    parser.add_argument('--operation',
                        type=str,
                        help='Operation to perform',
                        required=False)

    return parser.parse_args()


def main():

    args = get_user_args()
    fires = my_utils.get_column(args.file_name, args.country_column,
                                args.country, result_column=args.result_column)

    if len(fires) == 0:

        print('No fires found for query')
        
    elif args.operation == 'list':
        
        print(fires)

    elif args.operation == 'mean':

        print(f'Mean Fires in {args.country} is: '
              f'{my_utils.get_mean(fires):.3f}')

    elif args.operation == 'median':

        print(f'Median Fires in {args.country} is: '
              f'{my_utils.get_median(fires):.3f}')
    elif args.operation == 'standard deviation' and len(fires) > 1:

        print(f'Standard deviation of fires in {args.country} is: '
              f'{my_utils.get_standard_deviation(fires):.3f}')
    else:

        print(f'Total Fires in {args.country} between 1990 and 2020: '
              f'{sum(fires)}')


if __name__ == "__main__":
    main()
