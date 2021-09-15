#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def rep(x):
        return [x if x != search else replace]
    return list(map(rep, my_list))
    
