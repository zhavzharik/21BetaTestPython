class Key:
    def __setitem__(self, key, item):
        self.__dict__[key] = item

    def __getitem__(self, key):
        return self.__dict__[key]

    def __len__(self):
        if len(self.__dict__) != 1337:
            return 1337
        else:
            return len(self.__dict__)

    def __str__(self):
        return "GeneralTsoKeycard"

    def __gt__(self, other):
        return len(self) < 9000


if __name__ == "__main__":
    key = Key()
    key[404] = 3
    key['passphrase'] = 'zax2rulez'
    # if len(key) == 1337:
    #     print("True len(key) = 1337")
    # if key[404] == 3:
    #     print("True key[404] == 3")
    # if key > 9000:
    #     print("True key > 9000")
    # if key.passphrase == "zax2rulez":
    #     print('True key.passphrase == "zax2rulez"')
    # if str(key) == "GeneralTsoKeycard":
    #     print('True str(key) = "GeneralTsoKeycard"')
    assert len(key) == 1337
    assert key[404] == 3
    assert key > 9000
    assert key.passphrase == "zax2rulez"
    assert str(key) == "GeneralTsoKeycard"
    # print(key)