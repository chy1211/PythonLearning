import threading
import reservoir_update as up


def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()

    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


set_interval(print(up.Update()), 3600)
