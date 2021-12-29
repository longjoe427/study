import threading
import time

# gil
#在同一时刻，只能有1个线程在运行
# 多进程，并行；多线程为并发

# def task():
    # time.sleep(5)
    # print('thrown the second apple')
    # a=0
    # while a != 999*999:
    #     a += 1
    # print('ok')


# def task2():
#     print('thrown the third apple')


# def main():
#     start_time = time.time()
    # thread1=threading.Thread(target=task)
    # thread2=threading.Thread(target=task)
    # thread1.start()
    # thread2.start()
    # 让其他线程等自己执行完,使用jion；不使用jion，线程开始就开始计时
    # thread1.join()
    # thread2.join()
    # a = 0
    # while a != 999 * 999 *2:
    #     a += 1
    # end_time = time.time()
    # print(end_time-start_time)
    # print('thrown the first apple')

# if __name__ == '__main__':
#         main()
#
# num =2
# if num >1:
#     print('num<1')
# elif num > 100:
#     print('num <100')
#
# list = [1,2,3]
# list[2]
#
# dict ={'age':10}
# print(dict['age'])
# def div(a,b):
#     return a/b
# div(1,1)

# class MyException(Exception):
#     def __init__(self,msg):
#         self.msg = msg
#
# def set_age(num):
#     if num <=0 or num >200:
#         raise MyException(f'错误值：{num}')
#     else:
#         print(f'设置的年龄为：{num}')
#
# set_age(-2)

class Person():
    name = 'default'
    age = 0
    gender = 'male'
    weight = 0

    def __init__(self):
        print('ok')

    def set_atri(self,age):
        self.age = age


    def eat(self):
        print('eating')
        print(self.name)
    def play(self):
        print('playing')
    def jump(self):
        print('jump')

zk = Person()
# print(zk.name)
# zk.set_atri(20)
# print(zk.age)
