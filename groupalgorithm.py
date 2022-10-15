def func_1(n_customers):
    answer = {}
    for i in range(n_customers):
        group = 0
        i_str = str(i)
        for char in i_str:
            group += int(char)
        try:
            answer[group] += 1
        except KeyError:
            answer[group] = 1
    return answer


def func_2(n_customers, n_first_id):
    answer = {}
    for i in range(n_first_id, n_customers):
        group = 0
        i_str = str(i)
        for char in i_str:
            group += int(char)
        try:
            answer[group] += 1
        except KeyError:
            answer[group] = 1
    return answer


