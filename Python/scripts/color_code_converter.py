def rgb_formatter(value):
    """
    Formats iterable of 3 containing rgb values into CSS-valid output
    """

    if n:= len(value) != 3:
        raise NotImplemented(f"Expected iterable with 3 items, got {n}")
    return f"rgb({value[0]}, {value[1]}, {value[2]})"

def hex_to_rgb(value, formatted=True):
    """
    Converts hex code to rgb value.
    """

    if len(value) != 3 and len(value) != 6:
        raise NotImplemented("Invalid hex property passed")
    split_value = int(len(value) / 3)
    values = []
    while value != '':
        values.append(value[:split_value])
        value = value[split_value:]
    result = list()
    try:
        result = [int(i, 16) for i in values]
    except ValueError:
        raise NotImplemented("Invalid hex property passed")
    return rgb_formatter(result) if formatted else result

"""
def true_shader(value, ratio):
    result = []
    for i in range(3):
        result.append(
"""
#print(hex_to_rgb("222627"))
