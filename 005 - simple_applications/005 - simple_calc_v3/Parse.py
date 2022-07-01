# Parse - разбор текстовых строк
class Parse:
    # если в строке есть операнд '+-*/%' 
    # то обрезать конец строки до последнего операнда
    def back_to_operand(self, line: str) -> str:
        for operand in '+-*/%':
            pass