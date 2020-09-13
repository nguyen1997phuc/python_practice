# d = {}
# d.setdefault('a', []).append(1)

# d = {'a': 1, 'b': 2}
# print(d.get('c', 'hello world'))

# d = {'apple': 10, 'orange': 20, 'banana': 5, 'rotten tomato': 1}
# from operator import itemgetter
# d= sorted(d.items(), key=itemgetter(1))
# print(d)

# _dict_1 = {"one": 1, "two": 2}
# _dict_2 = {"three": 3, "four": 4, "five": 5}
# assert len(_dict_1) == len(_dict_2)
# print("hello world")


# def say_yolo(name):
#    print(f'Yolo {name}')
# exec('say_yolo', {'name': 'Phuc'})

# a, *_ = [{'a': 1}, {'b': 2}, {'c': 3}]
# print(a)

def with_dict(operator, x, y):
    return {
        'add': lambda: x+y,
        'sub': lambda: x-y
    }.get(operator, lambda: None)()


res = with_dict('add', 10, 20)
print(res)
