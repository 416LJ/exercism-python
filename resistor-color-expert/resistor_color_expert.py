def resistor_label(colors):
    color_array = colors_list()
    tols_list = tol_list()
    chart = {color_array[x] : x for x in range(len(color_array))}
    
    if len(colors) == 1:
        return f"{chart[colors[0]]} ohms"
    
    if len(colors) == 4:
        color_1 = colors[0]
        color_2 = colors[1]
        color_3 = colors[2]
        color_4 = colors[3]
        
        zeros = chart[color_3]
        tols_num = tols_list[color_4]
        tolerance = tols_num/100

        ohms = int(str(chart[color_1])+str(chart[color_2]))*((1*(10**zeros)))
        
        if ohms == 0:
            return f"{ohms} ohms"
        
        elif len(str(ohms)) >= 10 and len(str(ohms)) < 13:
            ohms = ohms/1000000000
            if ohms == int(ohms):
                return f"{int(ohms)} gigaohms ±{tols_num}%"
            return f"{ohms} gigaohms ±{tols_num}%"
        
        elif len(str(ohms)) >=7 and len(str(ohms)) < 10:
            ohms = ohms/1000000
            if ohms == int(ohms):
                return f"{int(ohms)} megaohms ±{tols_num}%"
            return f"{ohms} megaohms ±{tols_num}%"
        
        elif len(str(ohms)) >= 4 and len(str(ohms)) < 7:
            ohms = ohms/1000
            if ohms == int(ohms):
                return f"{int(ohms)} kiloohms ±{tols_num}%"
            return f"{ohms} kiloohms ±{tols_num}%"
        
        else:
            if ohms == int(ohms):
                return f"{int(ohms)} ohms ±{tols_num}%"
            return f"{ohms} ohms ±{tols_num}%"
            
        
    if len(colors) == 5:
        color_1 = colors[0]
        color_2 = colors[1]
        color_3 = colors[2]
        color_4 = colors[3]
        color_5 = colors[4]
        
        zeros = chart[color_4]
        tols_num = tols_list[color_5]
        tolerance = tols_list[color_5]/100

        ohms = int(str(chart[color_1])+str(chart[color_2])+str(chart[color_3]))*((1*(10**zeros)))
        
        if ohms == 0:
            return f"{ohms} ohms"
        
        elif len(str(ohms)) >= 10 and len(str(ohms)) < 13:
            ohms = ohms/1000000000
            if ohms == int(ohms):
                return f"{int(ohms)} gigaohms ±{tols_num}%"
            return f"{ohms} gigaohms ±{tols_num}%"
        
        elif len(str(ohms)) >=7 and len(str(ohms)) < 10:
            ohms = ohms/1000000
            if ohms == int(ohms):
                return f"{int(ohms)} megaohms ±{tols_num}%"
            return f"{ohms} megaohms ±{tols_num}%"
        
        elif len(str(ohms)) >= 4 and len(str(ohms)) < 7:
            ohms = ohms/1000
            if ohms == int(ohms):
                return f"{int(ohms)} kiloohms ±{tols_num}%"
            return f"{ohms} kiloohms ±{tols_num}%"
        
        else:
            if ohms == int(ohms):
                return f"{int(ohms)} ohms ±{tols_num}%"
            return f"{ohms} ohms ±{tols_num}%"
            
        
def colors_list():
    expected = [
            "black",
            "brown",
            "red",
            "orange",
            "yellow",
            "green",
            "blue",
            "violet",
            "grey",
            "white",
        ]
    return expected

def tol_list():
    expected2 = {
        'grey': 0.05,
        'violet': 0.1,
        'blue': 0.25,
        'green': 0.5,
        'brown': 1,
        'red': 2,
        'gold': 5,
        'silver': 10
    }
    return expected2