def itemgetter(key):
    return lambda obj: obj[key]

data = {"a": 1, "b": 2, 3: 4}

values = [5, 10, 15, 20]

itemgetter("b")(data)

get3 = itemgetter(3)

get3(values)

get3(data)

# ou
def itemgetter(key):
    def func(obj):
        return obj[key]
    return func

# ou
from operator import itemgetter
