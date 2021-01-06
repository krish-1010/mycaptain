list1 = [] 


n = int(input("Enter number of elements :"))



for i in range(0,n):
  ele = int(input())
  if ele > 0:
    list1.append(ele)
print("The positive numbers are: ",list1, end='')
