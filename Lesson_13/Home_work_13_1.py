from random import randint
from time import sleep
from threading import Thread
from time import time


start_time = time()
list = []
def stream():
    for i in range(1,1001):
        rand = randint(1,100000)
        sleep(0.000000000000000000000000000001)
        print(f'🔀  {i}')
        list.append(rand)

def sum_num():
    print(f'Sum of numbers: {sum(list)}')
def average():
    print(f'Average of numbers: {sum(list) / len(list)}')

def main():
    t1 = Thread(target=stream)
    t2 = Thread(target=sum_num)
    t3 = Thread(target=average)

    t1.start()
    t1.join()
    t2.start()
    t3.start()
    t3.join()
    print(f'Total time ⏳: {time() - start_time}')

if __name__ == "__main__":
    main()