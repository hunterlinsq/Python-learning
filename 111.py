# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 19:48:27 2017

@author: hunterlin
"""
'''
def calculate(self,n,A,B):
    if len(str(A))!=len(str(B)) or len(str(A))!=n:
        break
    else:
         print(int(str(abs(A-B))),2)
'''        
         


        
n = int(input())

l = input()

p = ("1","2","3","4","5","6","7","8","9")

start = 0

end = n-1

t = []

for i in range(n):

    if l[i] in p:

        start = i-int(l[i])

        if start < 0:

            start = 0

        end = i + int(l[i])

        if end >= n:

            end = n-1

        ll = l[start:(end+1)]

        ln = len(ll)

        for j in range(ln):

            if ll[j] == "X":

                	t.append(start+j)

out = set(t)

print len(out)





n=int(input())
a=str(input())
b=str(input())
c=[]
for i in range(n):
    c.append(abs(int(a[i])-int(b[i])))
d=0
for j in range(n):
    d=d+c[j]*(2**(n-j-1))
print int(d)