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
- Github workflows will run unit and functional tests upon push/pulls to
a remote repo
