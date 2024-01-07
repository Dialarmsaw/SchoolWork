num=int(input("Give me a whole number >>>"))

nums=[]

while True:
    nums.append(int(num))
    if nums[len(nums)-1]==1:
        break
    if num%2==0:
        num = num / 2
    elif num%2!=0:
        num = (num * 3)+1

biggest=0
for i in range(len(nums)):
    if nums[i]>biggest:
        biggest=nums[i]
print(nums, "it had a length of", len(nums), "and the biggest number was", biggest)
