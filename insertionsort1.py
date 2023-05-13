def insertionsort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp
    return arr
arr=[40,10,50,30,20,12,20]
print(insertionsort(arr))            