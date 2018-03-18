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
        return '1'


def get_neighbours_status(x, y, data):
    status = []
    try:
        status.append(data[x][y-1])
    except:
        pass

    try:
        status.append(data[x][y + 1])
    except:
        pass

    try:
        status.append(data[x-1][y])
    except:
        pass

    try:
        status.append(data[x+1][y])
    except:
        pass

    try:
        status.append(data[x-1][y-1])
    except:
        pass

    try:
        status.append(data[x-1][y+1])
    except:
        pass

    try:
        status.append(data[x+1][y-1])
    except:
        pass

    try:
        status.append(data[x+1][y+1])
    except:
        pass

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
