def hello():
    print("hello")

def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

def eat_lunch(food):
    if len(food) == 0:
        print("My lunchbox is empty!")
    else:
        print("First I eat " + food[0])
        for food in food[1:]:
            print("Next I eat " + food)

hello()
print(pack("a","b","c"))
eat_lunch([])
eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])