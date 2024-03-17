class Dict2:
    def __init__(self):
        self.items = []

    def __setitem__(self, key, value):
        for item in self.items:
            if item[0] == key:
                item[1] = value
                return
        self.items.append([key, value])

    def __getitem__(self, key):
        for item in self.items:
            if item[0] == key:
                return item[1]
        raise KeyError(f"Key '{key}' not found")

    def __iter__(self):
        for item in self.items:
            yield item[0]
