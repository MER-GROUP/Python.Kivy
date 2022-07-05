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
print('---------------------------')
print("float('0.'): " ,float('0.'))
print('---------------------------')
a = ''
print('a =' , a)
print('---------------------------')
print("float('-0.'): " ,float('-0.'))
print('---------------------------')
import re
my_st = "Я\nучу; язык,программирования\nPython"
print(re.split(';|,|\n', my_st)[-1])
print('---------------------------')
import re
my_st = "Я учу язык программирования Python"
print(re.split(';|,|\n', my_st)[-1])
print('---------------------------')
class Parse:
    def split(self, line: str) -> list[str]:
        import re
        return re.split('\+|\-|\*|\/|\%', line)

print(Parse().split('1212+67676-787878+8989898'))
print('---------------------------')