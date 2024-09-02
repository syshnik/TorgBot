import os
from time import sleep

path = "d:/BS/Save/WORK/Programm/bi/pyexe/dist/Go_run_606.exe"
del5=False
while del5==False:
    try:
        os.remove(path)
        del5=True
    except OSError:
        v1=OSError
        print("Надо закрыть программу Go_run_606.exe !")
        sleep(11)
        pass
print("Go_run_606.exe удален.")
