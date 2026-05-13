from collections import OrderedDict

cache = OrderedDict()
size = 3

operations = ["A", "B", "C", "A", "D"]

for item in operations:

    if item in cache:
        cache.move_to_end(item)

    else:
        if len(cache) >= size:
            cache.popitem(last=False)

        cache[item] = True

print("Cache:", list(cache.keys()))