from turtle import pensize


empty_list: list[str] = list()

# print(len(empty_list))

# print(empty_list[0])


# list = [1, 3, 5, 6, 7]

# print(list[0])
# print(list[len(list) - 1])
# print(list[len(list) // 2])

list = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

list[0] = 'NVIDIA'

# print(list)

# list.append('Silpo')

# print('#'.join(list))

# print(list.insert(20, 'CompanyOne'))

# print(list)

print('Google' in list)

number_list = [1, 2, 5, 30, 0, 9, 6]

copied_list = number_list.copy()

# number_list.sort(reverse=True)



# copied_list.reverse()

# print(copied_list)

# # print(copied_list[0:3])

# print(copied_list[len(copied_list) - 3:])


# copied_list.pop(0)
# copied_list.pop()

# print(copied_list)
# print(copied_list)

# copied_list.clear()

# print(copied_list)

# # del copied_list

# print(copied_list)


front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

print(front_end.extend(back_end))

joined_list = front_end + back_end

front_end.pop()


joined_list.insert(joined_list.index('Redux') + 1, 'SQL')

print(joined_list)


ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]


print(max(ages))

print(min(ages))

print(sum(ages) / len(ages))

print(abs(-5))


a, b, c, *rest = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

print(rest)