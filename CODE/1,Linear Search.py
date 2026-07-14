print("M Rakesh")
print("192421006")

def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = list(map(int, input("Enter array elements: ").split()))
key = int(input("Enter key to search: "))

result = linear_search(arr, key)

if result != -1:
    print("Key found at index", result)
else:
    print("Key not found")
