import time
n = 0
body = "|#O#O#O#|"

def derecha():
    for i in range(6, 15, 1):
        for k in range(4):
            print(body.rjust(i+2, " "))
        time.sleep(0.06)
    izquierda()
    
def izquierda():
    for j in range(15, 6, -1):
        for g in range(4):
            print(body.rjust(j+2, " "))
        time.sleep(0.06)
    derecha()
         
derecha()
    