# Easy Level
# Find largest number
arr=[3,7,1,5,9]
large=arr[0]
for num in arr:
    if num>large:
        large=num
print(large)
print("-"*20)
# Find smallest number
arr=[3,7,1,5,9]
small=arr[0]
for num in arr:
    if num<small:
        small=num
print(small)
print("-"*20)
# Find sum of array
sum_t=0
arr=[3,7,1,5,9]
for num in arr:
    sum_t+=num
print(sum_t)
print("-"*20)
# Count elements
count=0
arr=[3,7,1,5,9]
for num in arr:
    count+=1
print(count)
print("-"*20)
# Find average

# Beginner Interview Level
# Reverse array
arr=[1,2,3,4,5]
l=0
r=len(arr)-1
while l<r:
    arr[l],arr[r]=arr[r],arr[l]
    l+=1
    r-=1
print(arr)
print("-"*20)
# Reverse string
str1="abc"
li=list(str1)
l=0
r=len(li)-1
while l<r:
    li[l],li[r]=li[r],li[l]
    l+=1
    r-=1
li="".join(li)
print(li)
print("-"*20)
# Count vowels
st="raju"
count=0
for ch in st:
    if ch in "aeiou":
        count+=1
print(count)
    
print("-"*20)
# Find even numbers
arr=[1,2,3,4,5]
for num in arr:
    if num % 2==0:
        print(num)
        
print("-"*20)
# Find odd numbers
arr=[1,2,3,4,5]
for num in arr:
    if num % 2 !=0:
        print(num)
print("-"*20)
# second lagest number
arr=[3,7,1,5,9]

first_large=arr[0]
second_large=arr[1]

for num in arr:
    if num>first_large:
        second_large=first_large
        first_large=num
print(second_large)
        