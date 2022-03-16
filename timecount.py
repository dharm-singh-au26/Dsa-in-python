import time

# initial = time.time()

# k = 0
# while k<=100 :
#     print(k)
#     k += 1

# for i in range(0,101):
#     print(i)

# print(time.time()-initial)
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
