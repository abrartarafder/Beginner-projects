# insertion sort code: 
def insertion_sort(values):
    for j in range(1, len(values)):
        key = values[j]
        i = j - 1
        while i >= 0 and values[i] > key:
            values[i + 1] = values[i]        
            i -= 1
        values[i + 1] = key
    return values
    
    
    
unsorted = [8,19,-4,21,-13,0,6,-4]
sorted = insertion_sort(unsorted)
print(sorted)
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
