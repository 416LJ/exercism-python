def value(colors):
    color_array = colors_list()
    chart = {color_array[x] : x for x in range(len(color_array))}
    color_1 = colors[0]
    color_2 = colors[1]
    return int(str(chart[color_1])+str(chart[color_2]))

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
