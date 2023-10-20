test -e ssshtest || wget -q https://raw.githubusercontent.com/ryanlayer/ssshtest/master/ssshtest
. ssshtest

country="Afghanistan"
country_column=0
fires_column=3
data_path='../test_data/'
file_name="$data_path"'Agro_co2_emission_test.csv'

run basic_mean python ../../src/print_fires.py \
                    --country "$country" --country_column $country_column \
                    --result_column $fires_column --file_name $file_name \
                    --operation 'mean'
                    
assert_in_stdout 0
assert_exit_code 0

run basic_median python ../../src/print_fires.py \
                    --country "$country" --country_column $country_column \
                    --result_column $fires_column --file_name $file_name \
                    --operation 'median'
                    
assert_in_stdout 0
assert_exit_code 0

run basic_stdev python ../../src/print_fires.py \
                    --country "$country" --country_column $country_column \
                    --result_column $fires_column --file_name $file_name \
                    --operation 'standard deviation'
                    
assert_in_stdout 0
assert_exit_code 0
python ../../src/print_fires.py \
                    --country "$country" --country_column $country_column \
                    --result_column $fires_column --file_name $file_name \
                    --operation 'standard deviation'
run fileNotFound python ../../src/print_fires.py \
                    --country "$country" --country_column $country_column \
                    --result_column $fires_column --file_name bubba.csv \
                    --operation 'mean'
                    
assert_exit_code 1