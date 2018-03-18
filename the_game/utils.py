def will_alive(current_status, neighbours_status):
    living_cell = neighbours_status.count('1')
    if current_status == '1' and living_cell < 2:
        return '0'
    elif current_status == '1' and (living_cell == 2 or living_cell == 3):
        return '1'
    elif current_status == '1' and living_cell > 3:
        return '0'
    elif current_status == '0' and living_cell == 3:
        return '1'
    else:
        return current_status


def get_neighbours_status(x, y, xmax, ymax, data):
    status = []
    if not y-1 < 0:
        status.append(data[x][y-1])
    if not y+1 >= ymax:
        status.append(data[x][y + 1])
    if not x-1 < 0:
        status.append(data[x-1][y])
    if not x+1 >= xmax:
        status.append(data[x+1][y])
    if not (x-1 < 0 or y-1 < 0):
        status.append(data[x-1][y-1])
    if not (x-1 < 0 or y+1 >= ymax):
        status.append(data[x-1][y+1])
    if not (x+1 >= xmax or y-1 < 0):
        status.append(data[x+1][y-1])
    if not (x+1 >= xmax or y+1 >= ymax):
        status.append(data[x+1][y+1])

    return status


def string_to_array(x, y, data):
    clean_data = list(data.replace(',', '').replace(' ', ''))
    final_array = []
    clm = 0

    for row in range(x):
        final_array.append(clean_data[clm:clm+y])
        clm += y
    return final_array


def array_to_string(data):
    final_data = ""

    for row in data:
        final_data += ",".join(row)
        final_data += ","
    return final_data[:-1]
