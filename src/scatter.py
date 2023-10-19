import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
import csv

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
    parser.add_argument('--data_file_x',
                        type=str,
                        help='The name of the query country',
                        required=True)
    parser.add_argument('--data_file_y',
                        type=str,
                        help='The index of the column containing countries',
                        required=True)
    parser.add_argument('--y_label',
                        type=str,
                        help='Name of the y data',
                        required=True)
    parser.add_argument('--x_labels',
                        type=str,
                        help='X data fields',
                        required=True)
    return parser.parse_args()

def get_file_data(file_name):
    
    try:
        with open(file_name, 'r') as f:
            
            return f.readlines()
        
    except FileNotFoundError:
        print('Could not find ' + file_name)
        sys.exit(1)
    except PermissionError:
        print('Could not open ' + file_name)
        sys.exit(1)
    except TypeError:
        print('Error in converting query column to an integer')
        sys.exit(1)

def main():
    
    args = get_user_args()
    x_labels = args.x_labels.split()
    y_label = args.y_label   

    y = get_file_data(args.data_file_y)

    x = get_file_data(args.data_file_x)

    y_values = next(iter(y)).strip()
    y_values = [int(val) for val in y_values.split(',')]

    for idx, line in enumerate(x):

        
        x_values = line.strip()
        x_values = [int(val) for val in x_values.split(',')]

        x_label = x_labels[idx]    

        fig, ax = plt.subplots()
        ax.xaxis.set_major_locator(plt.MaxNLocator(3))
        ax.scatter(x_values,y_values)
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(f'{y_label}_vs_{x_label}')

        plt.savefig(f'../docs/{y_label}_vs_{x_label}.png',bbox_inches='tight')

if __name__ == "__main__":
    main()
