import queue

q1 = queue.Queue()     # 队列，先进先出
q1.put(1)
q1.get()
q1.put_nowait(2)
q1.get_nowait()

q2 = queue.LifoQueue()    # 栈，先进后出
q2.put(1)
q2.get()

q3 = queue.PriorityQueue()    # 优先级队列
q3.put((1, 'a'))    # 存入元组，元组的第一个值是优先级
q3.put((2, 'b'))
q3.put((3, 'c'))
print(q3.get())

