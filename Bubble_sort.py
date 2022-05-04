#Bubble sort 

def bubble_sort(lstt):
     for i in range(len(lstt)-1):
        for j in range(len(lstt)-1):
             if lstt[j]>lstt[j+1]:
                 lstt[j+1],lstt[j] = lstt[j], lstt[j+1]

lstt = [11,0,25,19,99,6]
bubble_sort(lstt)
print(lstt)




