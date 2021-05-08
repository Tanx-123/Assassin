import time
import threading
def square(number):
    print("Square of the number:")
    for i in number:
        time.sleep(0.2)
        print("Square:",i*i)
def cube(number1):
    print("cube of the number:")
    for i in number1:
        time.sleep(0.2)
        print("Cube of the nubmer:",i*i*i)
ar=[2,3,5,6]
t=time.time()
t1=threading.Thread(target=square,args=(ar,))
t2=threading.Thread(target=cube,args=(ar,))

t1.start()
t2.start()

t1.join()
t2.join()

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")