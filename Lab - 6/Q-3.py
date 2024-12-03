def my_max(data):
    max_value = None
    
    if isinstance(data, (list, set, tuple)):
        data = list(data)
        
        if len(data) > 0:
            max_value = data[0]
            
            for element in data[1:]:
                if element > max_value:
                    max_value = element
        else:
            return None 
    
    return max_value

list_data = [3, 1, 4, 1, 5, 9]
set_data = {7, 2, 8, 3}
tuple_data = (6, 3, 9, 2)

print("Maximum in list:", my_max(list_data))

print("Maximum in set:", my_max(set_data))

print("Maximum in tuple:", my_max(tuple_data))