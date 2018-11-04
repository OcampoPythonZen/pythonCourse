import threading
import time

def sleeper(n,name):
    print('Hi, I am {}. Going to sleep 5 sec.\n'.format(name))
    time.sleep(n)
    print('{} has woken up from sleep.\n'.format(name))
    

t = threading.Thread(target=sleeper,name='thread1',args=(5,'thread1'))
t1 = threading.Thread(target=sleeper,name='thread2',args=(4,'thread2'))
t2 = threading.Thread(target=sleeper,name='thread3',args=(3,'thread3'))

t.start()
t.join()
t1.start()
t1.join()
t2.start()
t2.join()


                      

#t.join() #Prevee ejecutar cualquier codigo hasta finalizar thread

#print('hello')
#print('hello1')
#print('hello2')

    
