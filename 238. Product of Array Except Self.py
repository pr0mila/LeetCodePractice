nums = [1,2,3,4]
prefix = []
suffix = []

for i in reversed(nums):
    if len(prefix) == 0:
        prefix.append(i)
        #print(i)
    else:
        product = prefix[-1] * i
        #print(prefix[-1])
        print(product)
#prefix = [k for k in reversed(prefix)]

