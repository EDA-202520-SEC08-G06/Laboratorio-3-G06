#Codigos para array list

def new_list():
    newlist={"elements":[], "size":0}
    return newlist


def get_element(my_list, index):
    return my_list["elements"][index]


def is_present(my_list, element, cmp_function):
    size=my_list["size"]
    if size>0:
        keyexist=False
        for keypos in range (0, size):
            info=my_list["elements"][keypos]
            if cmp_function(element,info)==0:
                keyexist=True
                break
        if keyexist:
            return keypos
    return -1



def add_first(my_list:array_list, element) -> array_list: 

    my_list["elements"] = [element] + my_list["elements"]
    my_list["size"] = my_list["size"] + 1 

    return my_list



def add_last(my_list:array_list, element) -> array_list:

    my_list["elements"] = my_list["elements"] + [element]
    my_list["size"] = my_list["size"] + 1 

    return my_list 



def size(my_list:array_list) -> int: 

    return my_list["size"]



def first_element(my_list:array_list): 

    return get_element(my_list, 0)



def is_empty(my_list:array_list) -> bool:

    if my_list["size"] == 0: 
        return True

    else:     
        return False



def last_element(my_list:array_list): 

    return get_element(my_list,my_list["size"]-1)



def delete_element(my_list:array_list, index:int) -> array_list: 

    
    if index <= my_list["size"] and index >= 0: 
        
        my_list["elements"] = my_list["elements"][:index] + my_list["elements"][index+1:] 
        my_list["size"] = my_list["size"] - 1
        
        return my_list
    
    else:
        return my_list



def remove_first (my_list:array_list):

    if is_empty(my_list): 
        return my_list

    else:
        my_list["size"] = my_list["size"] - 1
        return first_element(my_list), my_list



def remove_last (my_list:array_list):


    if is_empty(my_list): 
        return my_list

    else: 
        my_list["size"] = my_list["size"] - 1
        return last_element(my_list), my_list



def insert_element (my_list:array_list, element, index:int) -> array_list:

    if index > my_list["size"] or index < 0:  
        return my_list

    else:  
        my_list["elements"] = my_list["elements"][:index] + [element] + my_list["elements"][index:]
        my_list["size"] = my_list["size"] + 1
    
        return my_list



def change_info (my_list:array_list, index:int, new_info) -> array_list: 

    if index > my_list["size"] or index < 0:  
        return my_list

    else: 
         my_list["elements"] = my_list["elements"][:index] + [new_info] + my_list["elements"][index+1:] 
         my_list["size"] = my_list["size"]
         return my_list



def exchange (my_list:array_list, index1:int, index2:int) -> array_list:

    if (index1 > my_list["size"] or index1 < 0) or (index2 > my_list["size"] or index2 < 0):
        return my_list

    else:
        
        valor_index1 = my_list["elements"][index1:index]
        valor_index2 = my_list["elements"][index2:index2]

        my_list = my_list["elements"][:index1] + [valor_index2] + my_list["elements"][index1:index2] + [valor_index1] + my_list["elements"][index2:]
        
        return my_list



def sub_list (my_list:array_list, index:int, num_elements:int) -> array_list:   

    if index > my_list["size"] or index < 0:  
        return my_list

    else: 
        
        sub_list = {"elements": [], "size": 0}

        sub_list["elements"] = my_list["elements"][index:index+num_elements]
        sub_list["size"] = len(my_list["elements"])
        return sub_list



