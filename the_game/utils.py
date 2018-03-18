def is_alive(current_status, *args):
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
