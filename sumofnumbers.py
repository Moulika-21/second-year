def sum_of_list(lst):
    total = 0
    for n in lst:
        total = total  + int(n)
    return total  

# Test the function
print(sum_of_list([1, 2, '3', 4])) 
print(sum_of_list([1, 2, 3, 4, 5]))  
print(sum_of_list([]))  
