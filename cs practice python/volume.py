'''try:
    n = int(input("Enter a number: "))
    total = 0

    for i in range(1, n):
        total += i

    print(total)
except ValueError:
    print("Please enter a valid number!")'''

'''value = int(input())
count = 0 

for item in numbers:
    if item == value:
        count += 1
    
print(count)'''

'''word = input("Enter your word: ")
rev = ""

for i in range(len(word)-1,-1,-1):
    rev = rev + word[i]
    
print(rev)'''

'''numbers = [1,2,3,4,5,6,7,8]
sum = 0 
for i in numbers:
    if i % 2 == 0:
        sum += i
print(sum)

largest = numbers[0]  
smallest = numbers[-1]    
for z in numbers:
    if z > largest:
        largest = z
    if z < smallest:
        smallest = z
print(largest)
print(smallest)

text = input()
occ = 0 
for x in text:
    if x.isupper():
        occ += 1
print(f"There are {occ} numbers of Capital Letters")'''
word = input("Enter a word: ")
rle_list = []
count = 1

for i in range(1, len(word)):
    if word[i] == word[i - 1]:
        count += 1
    else:
        rle_list.append((word[i - 1], count))
        count = 1 


rle_list.append((word[-1], count))

res = str(rle_list)[1:-1].replace("'", '').upper()
print(res)
