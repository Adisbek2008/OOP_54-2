# итераторы

# __iter__() возвращает сам итератор
# __next__() возвращает следующий элемент или вызывает StopIteration

class Counter:

    def __init__(self, limit):
        self.limit = limit
        self.current = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < self.limit:
            num = self.current
            self.current += 1
            return num
        else:
            raise StopIteration


# for i in Counter(5):
#     print(i)

# генератор
def counter_up_to(limit):
    current = 0
    while current < limit:
        yield current
        current += 1

# for num in counter_up_to(5):
#     print(num)



# Big O

#
# tt = [1, 3, 46, 23, 24, 234 ,6, 4]

## Константная сложность
# def return_num(lst, index):
#     return limit(index)

# Линейная сложность
# def find_element(lst, target):
#     for i in lst:
#         if target == i:
#             return i
#     return "Нету"
#
# print(find_element(tt, 3))

# # Логарифмическая сложность
#
# def binary_search(lst, target):
#     left, right, = 0, len(lst) - 1
#
#     while left <= right:
#         mid = (left + right // 2)
#         if lst[mid] == target:
#             return mid
#         elif lst[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1
#
#     return "Нету"
#
#
# print(binary_search(array, 6))


# Квадратичная сложность
tt = [34, 23, 12, 4, 3, 21, 5, 1, 21, 4, 5, 3]
def bubbly_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubbly_sort(tt))


def two_sum(arr, target):
    num_map = {}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

nums = [2, 7, 11, 15]
print(two_sum(nums, 9))

