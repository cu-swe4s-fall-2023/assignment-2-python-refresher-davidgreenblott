
#takes in a file name and returns values in a column that match a query_value
def get_column(file_name, query_column, query_value, result_column = 1):
    
    matchingValues = []
    
    #open file robustly
    with open(file_name,'r') as f:
        
        for line in f:
            
            items = line.strip().split(',')
            
            #adds result column of interest to return block 
            #if query_column value matches query_value
            if items[query_column] == str(query_value):

                matchingValues.append(items[result_column])
            
    return matchingValues