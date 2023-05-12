def bubblesort(satya):
    n=len(satya)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if satya[j]>satya[j+1]:
                temp=satya[j]
                satya[j]=satya[j+1]
                satya[j+1]=temp
    return satya
satya=[10,90,20,9,8,4,5,100,13,25]
print(bubblesort(satya))                
