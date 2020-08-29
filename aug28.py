
list = [10, 15, 3, 7]
sum = 0

#user input k
value=""

k = input("Enter your value: ")
length= len(list)

for i in range(length):
    #print(i)
    for j in range(length-i-1):
        #print(i+j+1)
        sum = list[i] + list[i+j+1]
        if sum == k:
            value="True"
            print("True")
            break;

if not value:
    print("False")
