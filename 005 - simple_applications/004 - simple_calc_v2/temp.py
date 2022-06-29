for i in range(10):
    print(f'{i} = {chr(i)}')
print('---------------------------')
print(chr(183))
print('---------------------------')
print('float("09") =', float(" 09"))
# print('float("") =', float(""))
print('eval(100 % 50) =', eval('10 % 50'))
print('---------------------------')
# print("float('-'): " ,float('-'))
print("float('-0'): " ,float('-0'))
# print("float('.'): " ,float('.'))
print('---------------------------')
if -0.0:
    print(True)
else:
    print(False)
print('---------------------------')
if -0.0 == 0:
    print(True)
else:
    print(False)