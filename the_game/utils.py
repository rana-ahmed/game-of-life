def will_alive(current_status, *args):
    living_cell = args.count('1')

    if current_status == '1' and living_cell < 2:
        return '0'

    elif current_status == '1' and (living_cell == 2 or living_cell == 3):
        return '1'
    elif current_status == '1' and living_cell > 3:
        return '0'
    elif current_status == '0' and living_cell == 3:
        return '1'
    else:
        return '0'


def get_neighbours_status(me, X, Y, data):
    neighbors = lambda x, y: [(x2, y2) for x2 in range(x-1, x+2)
                               for y2 in range(y-1, y+2)
                               if (-1 < x <= X and
                                   -1 < y <= Y and
                                   (x != x2 or y != y2) and
                                   (0 <= x2 <= X) and
                                   (0 <= y2 <= Y))]
    neighbors_value = list(map(lambda coordinate: data[coordinate[0]][coordinate[1]], neighbors(me[0], me[1])))
    return neighbors_value


def string_to_array(x, y, data):
    clean_data = list(data.replace(',', '').replace(' ', ''))
    final_array = []
    clm = 0

    for row in range(x):
        print(row)
        final_array.append(clean_data[clm:clm+y])
        clm += y
    return final_array


def array_to_string(data):
    final_data = ""
    flag = True

    for row in data:
        final_data += ",".join(row)
        if flag:
            final_data += ","
            flag = False
    return final_data
