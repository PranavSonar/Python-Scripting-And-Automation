def create_cubes(n):
    result = []
    for x in range(n):
        yield (x**3)

# print(create_cubes(10))


# for x in create_cubes(100):
#     print(x)


# yield -- generator with is used to call when its need to be used


def simple_gen():
    for x in range(3):
        yield x


x = simple_gen()

# for x in simple_gen():
#     print(x)


# print(next(x))
# print(next(x))
# print(next(x))
# print(next(x))
# print(simple_gen().__next__())
# print(simple_gen().__next__())
# print(simple_gen().__next__())
# print(simple_gen().__next__())

y = ['a', 3, 12, 3, 34, 3]

gen=(item for item in y)
for i in range(y.__len__()):
    print(next(gen))