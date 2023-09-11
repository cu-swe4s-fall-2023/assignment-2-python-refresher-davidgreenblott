
def get_column(file_name, query_column, query_value, result_column):
    
    matchingValues = []
    #this makes sure that we close the file without the close command
    with open(file_name,'r') as f:
        
        for line in f:
            
            # print(line)
            items = line.strip().split(',')
            # data.append(items)
            # if items[1]=='1990':
            #     print('here')
           
            # print(items[query_column])
            if items[query_column] == str(query_value):
                # print('here')
                matchingValues.append(items[result_column])
            
    return matchingValues

print(get_column('Agrofood_co2_emission.csv',1,1990,3))