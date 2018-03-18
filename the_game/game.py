from .utils import string_to_array, get_neighbours_status, will_alive


def get_game_result(grid, ages):
    results = {}
    for age in ages:
        for i in range(1, age+1):
            data = results.get(str(i), grid.data)
            if type(data) == str:
                array = string_to_array(grid.x, grid.y, data)
            else:
                array = data
            for x in range(grid.x):
                for y in range(grid.y):
                    neighbors_status = get_neighbours_status(x, y, array)
                    array[x][y] = will_alive(array[x][y], neighbors_status)
            results[str(i)] = array
    return results
