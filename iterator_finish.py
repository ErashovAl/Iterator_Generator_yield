nested_list = [
	['a', 'b', 'c', []],
	['d', 'e', 'f', 'h', False],
	[1, 2, [None]]
]

class FlatIterator():

    def __init__(self, nested):
        self.nested = nested
        self.medium_list = []

    def extractor(self, iter_list):
        for item in iter_list:
            if isinstance (item, list):
                self.extractor(item)
            else:
                self.medium_list.append(item)

    def __iter__(self):
        self.extractor(self.nested)
        return self

    def __next__(self):
        if len(self.medium_list):
            return self.medium_list.pop(0)
        else:
            raise StopIteration

if __name__ == '__main__':

    for item in FlatIterator(nested_list):
        if isinstance(item, str):
            item = (f"'{item}'")    
        
        print(item)


    flat_list = [item for item in FlatIterator(nested_list)]
