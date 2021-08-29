from decorator import decorator_purse


@decorator_purse
def add_ingot(purse):
    new_purse = purse.copy()
    try:
        ingot = purse['gold_ingots'] + 1
        new_purse['gold_ingots'] = ingot
    #     new = {'gold_ingots': ingot}
    #     new_purse.update(new)
    except KeyError:
        new_purse.setdefault('gold_ingots', 1)
    return new_purse


@decorator_purse
def empty(purse):
    purse.clear()
    return purse


@decorator_purse
def get_ingot(purse):
    new_purse = purse.copy()
    try:
        ingot = purse['gold_ingots'] - 1
        if ingot >= 1:
            new_purse['gold_ingots'] = ingot
        else:
            new_purse = empty(purse)
    except KeyError:
        pass
    return new_purse


if __name__ == "__main__":
    purse = {"gold": 6}
    # print(f'Empty_purse: {empty(purse)}')
    print(f' {add_ingot(purse)}')
    print(f' {get_ingot(purse)}')

    # print(f'2 + add_ingots: {add_ingot({"gold_ingots": 2})}')
    # print(f'3 - get_ingots: {get_ingot({"gold_ingots": 3})}')
    # print(f'31 - get_ingots: {get_ingot({"gold_ingots": 31})}')
    # print(f'1 - get_ingots: {get_ingot({"gold_ingots": 1})}')
    # print(f'Empty_purse - get_ingots: {get_ingot(empty(purse))}')
    # print(f'Example from exercise: {add_ingot(get_ingot(add_ingot(empty(purse))))}')
    # print(f'another key + add_ingots: {add_ingot({"gol_ingot": 2})}')
    # print(f'another key + add_ingots: {get_ingot({"gol_ingot": 2})}')
