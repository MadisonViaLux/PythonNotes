import time
from lru_cache import LRUCache

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Setting the limit of the cache for the 10,000 names
lru = LRUCache(10000)

# Setting every name in the first list to the cache
for name in names_1:
    lru.set(name, True)

# Comparing every name in the second list to the names in the first (in cache)
# If there is a duplicate then append it to the duplicates list
for name2 in names_2:
    if lru.get(name2) != None:
        duplicates.append(name2)


end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")