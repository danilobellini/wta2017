class CountGets(object):
    count = 0

    def __getattr__(self, name):
        self.count += 1
        return name

cg = CountGets()

hasattr(cg, "count")

cg.count

hasattr(cg, "a")

cg.count

hasattr(CountGets, "a")

cg.count
