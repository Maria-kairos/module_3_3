def print_params(a = 1, b = 'Cool', c = True):
    print(a, b,c)

values_list = [1, True, 'Sun']
values_dict = {'a': 1, 'b': True, 'c': 'List'}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [34, False]
print_params(*values_list_2, 42)