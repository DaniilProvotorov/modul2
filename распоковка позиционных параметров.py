def print_params(a = 1, b= 'str', c = True):
    print(a, b, c)

values_list = ['onmyneck', 163, True]
values_dict = { 'a': 1243, 'b': 'gram', 'c': 'drad' }

values_list_2 = ['ise', 'spi']

print_params()
print_params( b = 25, c = [1, 2, 3])
print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 512)

