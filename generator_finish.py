
nested_list = [
	1, ['a', 'b', 'c', []],
	['d', 'e', ['f', 'h'], False],
	[1, 2, None]
]

def flatten_gen(nested):
    for item in nested:
        if not isinstance(item, list):
            yield item
        else:
            yield from flatten_gen(item)


def flat_output():
    for item in flatten_gen(nested_list):
        if isinstance(item, str):
            item = (f"'{item}'")
        print(item)

def list_comp():     
    return [item for item in flatten_gen(nested_list)]

if __name__ == '__main__':

    flat_output()

    print(list_comp())