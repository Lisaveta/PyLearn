
def simlpe_nums(num, m):
    """
    Алгоритм Эратосфена для определения простых чисел
    проверяем входит ли число num во множество простых чисел simple
    медленный для больших чисел
    возвращает список простых чисел до M
    """
    all_num = [x for x in range(2, m + 1)]
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
    return list(simple)

def divide(m):
    """Возвращает список делителей числа m"""
    div = []
    d = 2
    while d * d <= m:
        if m % d == 0:
            div.append(d)
            m //= d
        else:
            d += 1
    if m > 1:
        div.append(m)
    return div

n = int(input())
list_N = [x for x in range(4, n)] #список составных чисел N, которые могут быть представимы в виде произведения двух простых чисел.
div_list = list(map(divide, list_N)) #список делителей каждого элемента списка list_N
div_list_1 = [x for x in div_list if len(x) == 2]
print("Список составных числе меньше N, которые можно представить в виде произведений двух простых чисел такой: ", [x * y for x, y in div_list_1])
