#Codigos para single linked lists

def new_list():
    newlist={"first":None, "last":None, "size":0}
    return newlist

def get_element(my_list, pos):
    searchpos=0
    node=my_list["first"]
    while searchpos<pos:
        node=node["next"]
        searchpos+=1
    return node["info"]
    
    def is_present(my_list, element, cmp_function):
        is_in_array=False
        temp=my_list["first"]
        count=0
        while not is_in_array and temp is not None:
            if cmp_function(element,temp["info"])==0:
                is_in_array= True
            else:
                temp=temp["next"]
                count+=1
        if not is_in_array:
            count=-1
        return count 
    
    