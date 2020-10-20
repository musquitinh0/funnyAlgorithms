def mergeSort(aList):
    print("Splitting...", aList)
    if len(aList) > 1:
        mid = len(aList)//2
        lefthalf = aList[:mid:]
        righthalf = aList[:mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)
        i = 0
        j = 0
        k = 0

    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            aList[k] = lefthalf[i]
            i += 1

        else:
            aList[k] = righthalf[j]
            j += 1
            k += 1

        while i < len(lefthalf):
            aList[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            aList[k] = righthalf[j]
            j += 1
            k += 1

    print("Merging... ", aList)


n = int(input("Enter number of elements : ")) 
arr = list(map(int,input("\nEnter the numbers : ").strip().split()))[:n] 

mergeSort(arr)
print(arr)
