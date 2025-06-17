def label(colors):
    color_array = colors_list()

    chart = {color_array[x] : x for x in range(len(color_array))}

    color_1 = colors[0]
    color_2 = colors[1]
    color_3 = colors[2]
    zeros = chart[color_3]
    print(color_1,color_2,color_3)
    ohms = int(str(chart[color_1])+str(chart[color_2]))*((1*(10**zeros)))

    if ohms == 0:
        return f"{ohms} ohms"
    elif ohms % 1000000000 == 0:
        ohms = int(ohms/1000000000)
        print(ohms)
        return f"{ohms} gigaohms"
    elif ohms % 1000000 == 0:
        ohms = int(ohms/1000000)
        print(ohms)
        return f"{ohms} megaohms"
    elif ohms % 1000 == 0:
        ohms = int(ohms/1000)
        print(ohms)
        return f"{ohms} kiloohms"
    else:
        return f"{ohms} ohms"

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
print(label(["red", "green", "yellow", "yellow", "brown"]))