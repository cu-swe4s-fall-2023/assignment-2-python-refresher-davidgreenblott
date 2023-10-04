#!/bin/bash

set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail #fail if any prior step failed
chmod +x run.sh
echo "Running print_fires.py"

country="United States of America"
country_column=0
fires_column=3
file_path='../data/'
file_name="$file_path"'Agrofood_co2_emission.csv'
python print_fires.py --country "$country" --country_column $country_column \
                      --fires_column $fires_column --file_name $file_name \
                      --operation 'mean'
