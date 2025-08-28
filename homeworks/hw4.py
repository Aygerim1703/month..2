from datetime import datetime as dt
def checktime(func):
    def wrapper(*args, **kwargs):
        timenow = dt.now()
        print(f"Функция была вызвана {timenow.year} : {timenow.month:2} : {timenow.day:2} :  {timenow.hour:2} : {timenow.minute:2} : {timenow.second:2} ")
        return func(*args, **kwargs)
    return wrapper
@checktime
def helloworld():
    print("hello world")

helloworld()