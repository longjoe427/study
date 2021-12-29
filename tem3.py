import threading
import time


# 迭代生成器:节省内存
#
# a = [0,1,2,3,4,5]
# b=[]
# for i in a:
#     i+=1
#     print(i)
#     b.append(i)
#     print(b)

# for index,i in enumerate(a):
#     a[index] += 1
#     print(a)

# a = map(lambda x:x+1,a)
# print(a)
# a.__next__()
# for i in a:
#     print(i)
# a = ( i+1 for i in range(10))
# print(a)
# print(type(a))

# def f(x):
#     return x*x
# z=map(f,a)
# print(map(f,a))
#
# for i in z:
#     print(i)

# b = [4,5,6]
# l = zip(a,b)
# print(l)
# print(*l)

# yield 保存程序的中断状态
# def fib(count):
#     n,a,b = 0,0,1
#     while n < count:
#         yield b
#         # print(b)
#         a,b = b,a+b
#         n = n+1
    # return 'done'
#
#
# f=fib(9)
# print(f)
# print(f)
# for f in fib(10):
#     print(f)
# while True:
#     try:
#         x = next(f)
#         print('f',x)
#     except StopIteration as e:
#         print('Generator return value:',e.value)
#         break

# print(next(f))
# print('====')
# print(next(f))


# print(f.__next__())
# print(f.__next__())
# print(f.__next__())
# print(f.__next__())

# def consumer(name):
#     print('%s准备吃包子了'%name)
#     while True:
#         baozi = yield
#         print("[%s]包子来了，被[%s]吃了"%(baozi, name))

# c =consumer('jk')
# c.__next__()
# # c.__next__()
#
# b1 = '韭菜馅'
# c.send(b1)

# def producer():
#     c = consumer('kk')
#     c2 = consumer('ll')
#     print('开始准备做包子啦')
#     c.__next__()
#     c2.__next__()
#     for i in range(10):
#         time.sleep(1)
#         print('做了俩baozi')
#         c.send(i)
#         c2.send(i+1)
#
# producer()
# from collections import Iterator, Iterable
#
# # print(isinstance(1, Iterator))
# # print(isinstance(( x for x in range(10)), Iterable))
# print(isinstance([1, 2, 3], Iterable))
# def run(n):
#     print('task',n)
#     time.sleep(2)
#
# t1 = threading.Thread(target=run,args=('t1',))
# t2 = threading.Thread(target=run,args=('t2',))
# t1.start()
# t2.start()

# run('t1')
# run('t2')

# class MyThread(threading.Thread):
#     def __init__(self,n):
#         super(MyThread,self).__init__()
#         self.n = n
#
#     def run(self):
#         print('runnit task',self.n)
#         time.sleep(2)
#
# t1= MyThread('t1')
# t2= MyThread('t2')
#
# # 顺序执行
# # t1.run()
# # t2.run()
#
# # 并行
# t1.start()
# t2.start()

def run(n):
    print('task',n)
    time.sleep(2)
    print('task done',threading.current_thread())

start_time = time.time()
t_objs = []
for i in range(50):
    t = threading.Thread(target=run,args=('t-%s'%i,))
    t.setDaemon(True) # 把当前现成设置为守护线程；主线程不需要等待子线程执行，与子线程并行
    t.start()
    t_objs.append(t)

for t in t_objs:
    t.join()  # 主线程依赖子线程完成后执行

print('---all is finished...',threading.current_thread(),threading.activeCount())
end_time = time.time()

print('cost time:', end_time - start_time)









