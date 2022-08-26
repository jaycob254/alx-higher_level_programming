def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    l_ist = [x for x in my_list]
    l_ist[idx] = element
    return (l_ist)
