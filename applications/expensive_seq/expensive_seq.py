# Your code here
cache = {}

def expensive_seq(x, y, z):
    global cache
    return_value = 0
    key = f'{x}, {y}, {z}'
    if key in cache:
        return cache[key]
    elif x <= 0:
        return_value = y + z
    else:
        return_value = expensive_seq(x - 1, y - 1, z)\
            + expensive_seq(x - 2, y + 2, z * 2)\
            + expensive_seq(x - 3, y + 3, z * 3)

    cache[key] = return_value
    return return_value

if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
