#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


from collections import deque
queue = deque()       # 创建空队列
for x in range(1,6):
	queue.append(x)   # 入队
	print('push', x, end=' ')
	print(list(queue))

print('Now queue is', list(queue))

while len(queue)>0:
	print('pop', queue.popleft(), end=' ')  # 出队
	print(list(queue))
