stuff_list = {'earphones': (400, 50), 'lighter': (300, 40),
              'math_book': (350, 50), 'physics': (200, 15),
              'bottle_of_water': (500, 450), 'laptop': (1300, 900),
              'sandwitch': (200, 800)}


def get_weight_and_value(stufflist):
    weights = [stufflist[item][0] for item in stufflist]
    values = [stufflist[item][1] for item in stufflist]
    return weights, values


def get_memory_table(stufflist, max_weight=2000):
    weights, values = get_weight_and_value(stufflist)
    table_dim = len(weights)

    main_table = [[0 for j in range(max_weight + 1)] for i in
                  range(table_dim + 1)]
    for i in range(table_dim + 1):
        for j in range(max_weight + 1):
            if i == 0 or j == 0:
                main_table[i][j] = 0

            elif weights[i - 1] <= j:
                main_table[i][j] = max(
                    values[i - 1] + main_table[i - 1][j - weights[i - 1]],
                    main_table[i - 1][j])

            else:
                main_table[i][j] = main_table[i - 1][j]

    return main_table, weights, values


def get_need_elem(stufflist, max_weight=2000):
    main_table, weights, values = get_memory_table(stufflist)
    table_size = len(weights)
    last_elem = main_table[table_size][
        max_weight]  # начало с последнего элемента
    max_of_weights = max_weight
    item_list = []  # Необходимый список площадей и ценностей

    for i in range(table_size, 0, -1):
        if last_elem <= 0:
            break  # Стоп, тк рюкзак полон
        if last_elem == main_table[i - 1][max_of_weights]:
            continue
        else:
            item_list.append((weights[i - 1], values[i - 1]))
            last_elem -= values[i - 1]
            max_of_weights -= weights[i - 1]

    need_stuff = []
    for nick in item_list:
        for key, value in stufflist.items():
            if value == nick:
                need_stuff.append(key)

    return need_stuff


def total(stufflist):
    stuff = get_need_elem(stufflist)
    total_weight = sum([stufflist[item][0] for item in stuff])
    total_value = sum([stufflist[item][1] for item in stuff])

    print(f'Total weight - {total_weight}, \nTotal value - {total_value} \nAll stuff: {stuff}')


def main():
    total(stuff_list)


if __name__ == "__main__":
    main()
