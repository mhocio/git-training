import  random

random_items = [random.randint(0,100) for c in range(10)]

def insertion_sort(items):
    count = 0
    for i in range(1, len(items)):
        j = i
        # count += 1
        while j > 0 and items[j] < items[j-1]:
            items[j], items[j-1] = items[j-1], items[j]
            j -= 1
            count += 1
        
        print(i, count, items)
    return count


count = insertion_sort(random_items)
print(random_items)
print(count)

print("test")


