#N = int(input())
num = 25
def simlpe_nums(num):
    """
    Алгоритм Эратосфена для определения простых чисел
    проверяем входит ли число num во множество простых чисел simple
    медленный для больших чисел
    """
    all_num = [x for x in range(2, num + 1)]
    no_simple = []
    for i in range(0, len(all_num)):
        j = 0
        for j in range(0, len(all_num)):
            if all_num[j] % all_num[i] == 0 and all_num[j] / all_num[i] != 1:
                no_simple.append(all_num[j])
            j += 1
    set_all_num = set(all_num)
    set_no_simple = set(no_simple)
    simple = set_all_num.difference(set_no_simple)
    return num in simple
