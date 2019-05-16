#python输出菱形
#coding=utf-8
from sys import stdout
for i in (0,1,2,3):
    for j in range(2-i+1):
        stdout.write(' ')
    for k in range(2*i+1):
        stdout.write('*')
    print()

for i in (0,1,2):
    for j in range(i+1):
        stdout.write(' ')
    for k in range(4-2*i+1):
        stdout.write('*')
    print()
