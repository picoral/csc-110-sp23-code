def main():
    items = [[9, 7, 8], 
             [5], 
             [10, 20, 30]]
    
    # [9, 7, 8, 5, 10, 20 , 30]
    
    # for every index for every list in outer list
    for i in range(len(items)):
        # for every index in each inner list
        for j in range(len(items[i])):
            # print every single item
            print( items[i][j] )
    
main()