#！/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = caicaizhang


'''
ref blog:
http://www.codebelief.com/article/2017/02/python-advanced-programming-list-comprehensions/

当然，在实际的应用中不能单纯追求代码的简洁，还要考虑到代码的可读性和维护成本。
如果代码变得过于复杂，不易于理解，我们宁可多写几行代码来增加它的可读性。

'''

# mat=[[j*i for j in range(1,4) for i in range(1,4)] for l in range(3)]
mat=[[x +i  for i in range(3)] for x in [j for j in range(9) if j % 3 ==1] ]


print('mat is:{}'.format(mat))

# mat = [[1,2,3], [4,5,6], [7,8,9]]
# new_mat = [ [row[i] for row in mat] for i in range(3)] # 嵌套
# print(new_mat)