from functional_purse import add_ingot, empty


def zero_ingots(purse):
    try:
        if purse['gold_ingots'] == 0:
            purse = empty(purse)
    except KeyError:
        pass
    return purse


def split_booty(*args):
    ingot = 0
    purse_1 = {}
    purse_2 = {}
    purse_3 = {}
    for purse in args:
        for key, value in purse.items():
            try:
                if key == 'gold_ingots':
                    ingot += value
                    # print(f'Ingot = {ingot}')
            except KeyError:
                ingot = 0
    purse_1['gold_ingots'] = ingot // 3
    purse_2 = purse_1.copy()
    purse_3 = purse_1.copy()
    if ingot % 3 == 2:
        purse_2 = add_ingot(purse_2)
        purse_3 = add_ingot(purse_3)
    elif ingot % 3 == 1:
        purse_2 = add_ingot(purse_2)
    purse_1 = zero_ingots(purse_1)
    purse_2 = zero_ingots(purse_2)
    purse_3 = zero_ingots(purse_3)
    return purse_1, purse_2, purse_3


if __name__ == "__main__":
    print("12 ingots:")
    answer_1, answer_2, answer_3 = split_booty({"gold_ingos": 3}, {"gold_ingots": 7}, {"gold_ingots": 5})
    print(answer_1, answer_2, answer_3, sep='\n')
    print("45 ingots:")
    # args = "{"gold_ingos": 3}, {"gold_ingots": 5}, {"gold_ingots": 35}, {"gold_ingots": 5}"
    # answer_1, answer_2, answer_3 = split_booty(*args)
    answer_1, answer_2, answer_3 = split_booty({"gold_ingos": 3}, {"gold_ingots": 5}, {"gold_ingots": 35}, {"gold_ingots": 5})
    print(answer_1, answer_2, answer_3, sep='\n')
    # print("41 ingots:")
    # answer_1, answer_2, answer_3 = split_booty({"gold_ingos": 3}, {"gold_ingots": 6}, {"gold_ingots": 35})
    # print(answer_1, answer_2, answer_3, sep='\n')
    # print("0 ingots:")
    # answer_1, answer_2, answer_3 = split_booty({"gold_ingos": 0}, {"gold_ingots": 0}, {"gold_ingots": 0})
    # print(answer_1, answer_2, answer_3, sep='\n')
    # print("1 ingots:")
    # answer_1, answer_2, answer_3 = split_booty({"gold_ingos": 0}, {"gold_ingots": 1}, {"gold_ingots": 0})
    # print(answer_1, answer_2, answer_3, sep='\n')
    # print("2 ingots:")
    # answer_1, answer_2, answer_3 = split_booty({"gold_ingos": 0}, {"gold_ingots": 2}, {"gold_ingots": 0})
    # print(answer_1, answer_2, answer_3, sep='\n')
    # print("Another dict:")
    # answer_1, answer_2, answer_3 = split_booty({"stone": 5}, {"apple": 6}, {"gold": 7})
    # print(answer_1, answer_2, answer_3, sep='\n')



