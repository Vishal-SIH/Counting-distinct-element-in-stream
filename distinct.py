arr = input("Input the stream elements separated by space ")
arr = arr.split(" ")

arr = [int(i) for i in arr]
# print(arr)
window = int(input("Please enter the window size "))

if(window > len(arr)):
	diff = 1
else:
	diff =len(arr) - window +1

print("Number of Distinct Elements in each window are ")
for i in range(0,diff):
	n = len(list(set(arr[i:i+window])))

	print("Window",i+1,":",n)

