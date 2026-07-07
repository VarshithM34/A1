import threading
import time

'''def func(seconds):
    print(f"Sleeping for {seconds} seconds...")
    time.sleep(seconds)
    
#func(3)
#func(2)
#func(1)
   
t1 = threading.Thread(target=func, args=(3,))
t2 = threading.Thread(target=func, args=(2,))   
 
t3 = threading.Thread(target=func, args=(1,))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()'''
def walk_park():
    time.sleep(3)
    print("Walking in the park...")
    
def cook_maggie():
    time.sleep(2)
    print("Cooking Maggie...")

def sleep():
    time.sleep(6)
    print("Sleeping...")
    
t1 = threading.Thread(target=walk_park)
t2 = threading.Thread(target=cook_maggie)   
t3 = threading.Thread(target=sleep)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("All tasks completed...")

semaphore = threading.Semaphore(2)
'''def walk_park():
    with semaphore:
        time.sleep(3)
        print("Walking in the park...")
    
def cook_maggie():
    with semaphore:
        time.sleep(2)
        print("Cooking Maggie...")

def sleep():
    with semaphore:
        time.sleep(6)
        print("Sleeping...")
    
t1 = threading.Thread(target=walk_park)
t2 = threading.Thread(target=cook_maggie)   
t3 = threading.Thread(target=sleep)
t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()
print("All tasks completed...")'''