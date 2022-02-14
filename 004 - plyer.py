# модуль для работы с вибрацией устройства
from plyer import vibrator

# делаем исключение NotImplementedError, NotImplementedError 
# (если телефон то вызвать вибрацию иначе выдать сообщение)
try:
    #вызов вибрации на 10 секунд
    vibrator.vibrate(10)
except (ModuleNotFoundError, NotImplementedError):
    print(ModuleNotFoundError('Устройство не телефон'))
    print(NotImplementedError('В Linux Debian не предусмотрена вибрация'))