def color_code(color):
    color_array = colors()
    chart = {color_array[x] : x for x in range(len(color_array))}
    return chart[color]


def colors():
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

print(colors())
print(color_code("white"))