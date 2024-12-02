def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(True, 'str', 1)
print_params()
print_params(1, 2)
print_params(b = 25)
print_params(c = [1, 2, 3])

values_list = [1, False, 2.34]
values_dict = {'a' : 11, 'b' : 3.1415, 'c': False}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [False, 'Adadad' ]
print_params(*values_list_2, 42)