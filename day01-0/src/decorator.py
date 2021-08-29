def decorator_purse(my_func):
    def wrapper(purse):
        print('SQUEAK')
        return_value = my_func(purse)
        return return_value
    return wrapper


if __name__ == "__main__":
    from functional_purse import add_ingot, empty, get_ingot
    purse = {"gold_ingots": 2}
    print(f'Example from exercise: {add_ingot(get_ingot(add_ingot(empty(purse))))}')




