# all combinations

# 1) variant with time error

# def update_number(lst, max_lst, new_index):
#     lst[new_index] += 1
#
#     if lst[new_index] > max_lst[new_index]:
#         lst[new_index] -= 1
#
#     i = 1
#     while new_index + i < len(lst):
#         lst[new_index + i] = lst[new_index] + i
#         i += 1
#
#     if lst[new_index] == max_lst[new_index]:
#         if i >= 2:
#             new_index -= (i - 1)
#         else:
#             new_index -= 1
#
#     return lst, new_index + (i - 1)
#
#
# def print_line(lst):
#     line = ""
#     for i in lst:
#         line += str(i) + " "
#     print(line)
#
#
# def combinations(n, k):
#     if not n > k:
#         print(0)
#         return 0
#
#     lst = [i for i in range(k)]
#     max_lst = [i for i in range(n - k, n)]
#     index = k - 1  # last index of list
#
#     print_line(lst)
#
#     while index >= 0:
#         if lst[index] == max_lst[index]:
#             lst, index = update_number(lst, max_lst, index - 1)
#             if lst == max_lst:
#                 print_line(lst)
#                 break
#         else:
#             lst[index] += 1
#
#         print_line(lst)
#
#


# More optimal variant
def task(lst, index, k, n):
    if index == k:
        print(*lst)
        # return
    else:
        for i in range(index, n - (k - index) + 1):
            lst[index] = i
            flag = True
            for j in range(k - 1):
                if lst[j] >= lst[j + 1]:
                    flag = False
                    break

            if flag:
                task(lst, index + 1, k, n)


def combinations(n, k):
    if n > k:
        lst = [i for i in range(k)]
        task(lst, 0, k, n)
    else:
        print(0)


# test
n = 7
k = 4

combinations(n, k)


# other variants

# 1)
# import itertools
#
#
# k, n = [int(i) for i in input().split()]
# m = list(itertools.combinations(range(n), k))
#
# for i in range(len(m)):
#     print(*m[i])

# 2)
# k, n = map(int, input().split(' '))
# lst = []
#
#
# def gen(i):
#     if len(lst) == k:
#         print(*lst)
#     for j in range(i):
#         lst.append(j)
#         gen(j)
#         lst.pop()
#
# gen(n)

