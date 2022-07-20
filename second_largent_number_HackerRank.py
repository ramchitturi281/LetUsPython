n=5
arr=[12,23,6,6,5]

print(arr)

new_arr=list(set(arr))
print(new_arr)
new_arr.sort()
print(new_arr)
print(new_arr[-2])


n=5
arr=[2,3,6,6,5]
print(n)
print(arr)
arr2=set(arr)
print(type(arr2))
print(arr2)
arr2.remove(max(arr2))
print(arr2)
print(max(arr2))