# https://cses.fi/problemset/task/2205

num = int(input())
for i in range(num*2):
    print(format(i, "0"+str(num)+"b"))