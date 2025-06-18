def is_paired(input_string):
    bracket_map = { "]" : "[", "}" : "{", ")" : "(" }
    full_list = []
    for i in input_string:
        print(i)
        if i in bracket_map.values():
            full_list.append(i)
            print(full_list)
        elif i in bracket_map:
            if len(full_list) == 0 or full_list.pop() != bracket_map[i]:
                    return False
            
    if len(full_list) == 0:
        return True
    else:
         return False         
            



is_paired("(){})()")