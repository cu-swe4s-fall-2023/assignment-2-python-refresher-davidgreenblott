import my_utils
import argparse
import os
import csv


def get_user_args():
    """Accepts user input from command line
    Parameters
    ----------
    Returns
    -------
    parser
    arg parser with country, country_column, result_column,
    file_name, and save_file_name fields
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
                        type=str,
                        help='Column containing data of interest',
                        required=True)
    parser.add_argument('--file_name',
                        type=str,
                        help='The file name',
                        required=True)
    parser.add_argument('--save_file_name',
                        type=str,
                        help='The save file name',
                        required=True)
    return parser.parse_args()


def main():

    args = get_user_args()
    col_index = my_utils.get_column_from_name(file_name=args.file_name,
                                              column_name=args.result_column)
    data = my_utils.get_column(args.file_name, args.country_column,
                               args.country, result_column=col_index)

    if len(data) == 0:

        print('No data found for query')

    else:

        with open(args.save_file_name, 'a+', newline='') as file:
            writer = csv.writer('../docs/'+file)
            writer.writerow(data)


if __name__ == "__main__":
    main()
