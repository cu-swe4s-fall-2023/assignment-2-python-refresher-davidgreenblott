[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# Python Refresher Assignment
Accepts user argument for a country and outputs the total number of fires between 1990 and 2020 for that country

# Organizational Requirements
- requires a csv file to be in the "data" folder that is on the same level as the "src" folder

# How to Use
1. put data in another folder on same level called "data"
2. `git clone https://github.com/cu-swe4s-fall-2023/assignment-2-python-refresher-davidgreenblott.git`
3. Query searching
a. specify the query locations for the country and fire columns
b. specify country of interest and file name
c. pass arguments upon running `print_fires.py`
4. Can also specify operation to perform on the list of integers that is returned 
a. options include setting the operation parameter to `mean`, `median`, or `standard deviation`

# Unit and Functional Testing
- Ensure you are running unit tests from the `tests/unit` directory
-  Ensure you are running functional tests from the `tests/func` directory
    -use the `test_print_fires.sh` script to run these
    
# Continuous Integration
- Github workflows will run unit and functional tests upon push/pulls to a remote repo

# Science Presentation
## Introduction
It was examined whether there was a correlation between forest fires and Industrial Processes and Product Use (IPPU), Forestland, and total emissions for Albania

## Methods
Data was extracted from the Agrofood_co2_emission.csv for each of the four fields. The forest fire data was plotted against each of the three other fields to examine
correlations.

## Results
1. There was a positive correlation between Forest Fires and Forestland
- this seems to be against logic
2. There was a negative correlation between Forest Fires and IPPU
3. There didn't eem to be too much of a correlation between Forest Firest and total emissions