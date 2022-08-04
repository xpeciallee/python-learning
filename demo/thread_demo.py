import threading
import time


def fun01(name):
    print('hello start', name)
    time.sleep(3)
    print('hello', name)


g_num = 0


def work1(thread_num):
    global g_num
    for i in range(100):
        g_num += 1
    print(f'g_num in work1 {thread_num} is {g_num}')


def work2(thread_num):
    global g_num
    for i in range(100):
        g_num += 1
    print(f'g_num in work2 {thread_num} is {g_num}')


if __name__ == '__main__':
    # 多线程
    t1 = threading.Thread(target=fun01, args=('t1',))
    t2 = threading.Thread(target=fun01, args=('t2',))
    t1.setDaemon(True)
    t2.setDaemon(True)  # 设置守护线程，当主线程结束，守护线程也将马上结束
    t1.start()
    t2.start()
    t1.join()  # 主线程等待守护线程结束
    print('end')

    '''
        多线程共享全局变量
        线程时进程的执行单元，进程时系统分配资源的最小执行单位，所以在同一个进程中的多线程是共享资源的
    '''

    w1 = threading.Thread(target=work1, args=('w1',))
    w2 = threading.Thread(target=work2, args=('w2',))
    w1.start()
    w2.start()
