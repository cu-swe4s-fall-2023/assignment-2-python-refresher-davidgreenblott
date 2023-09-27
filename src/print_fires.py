'''Prints out the total number of fires for a given country
    * get_user_args() - accepts user input from command line
    * main() - calls get_column() to find query result'''

from my_utils import get_column
import argparse


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
    parser.add_argument('--fires_column',
                        type=int,
                        help='The index of the column containing fire data',
                        required=True)
    parser.add_argument('--file_name',
                        type=str,
                        help='The file name',
                        required=True)

    return parser.parse_args()


def main():

    args = get_user_args()
    fires = get_column(args.file_name, args.country_column,
                       args.country, result_column=args.fires_column)
    totalFires = 0

    for fire in fires:
        totalFires += float(fire)
    print(f'Total Fires in {args.country} between 1990 and 2020: {totalFires}')


if __name__ == "__main__":
    main()
