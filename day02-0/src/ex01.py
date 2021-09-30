from collections import Counter


class Game(object):
    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()
        self.player = {}
        self.players = []
        self.partners = []

    # print result
    def __str__(self):
        return f'{self.registry.most_common(5)}'

    def gen_list_players(self):
        for name in [Cheater, Cooperative, Copycat, Grudger, Detective]:
            self.player = name()
            self.players.append(self.player)

    def update_registry(self, player1, player2):
        self.registry[player1.name] += player1.candy
        self.registry[player2.name] += player2.candy

    def play(self, player1, player2):
        # simulate number of matches equal to self.matches
        while self.matches > 0:
            player1.update_candy(player2)
            player1.record_behave()
            player2.record_behave()
            player1.update_behave(player2)
            player2.update_behave(player1)
            self.matches -= 1
        self.update_registry(player1, player2)
        player1.update_state()
        player2.update_state()
        self.update_matches()

    def update_matches(self):
        self.matches = 10

    def top3(self):
        # return top three (print top three winners after the whole game)
        for key, value in self.registry.most_common(3):
            print(key, value)

    def all_game(self):
        # simulate game 10 matches (one call of play())
        # between every pair of two players with different behavior types
        self.gen_list_players()
        for player1 in self.players:
            self.partners.append(player1.name)
            for player2 in self.players:
                if player1.name != player2.name and player2.name not in self.partners:
                    self.play(player1, player2)


class Player:
    def __init__(self):
        self.name = 'name'
        self.candy = 0
        self.prev = 2  # previous behave
        self.behave = 2  # (current behave) 1-cooperate, 0-cheat, 2 - no one

    def __str__(self):
        return f'{self.name}'

    def record_behave(self):
        self.prev = self.behave

    def update_candy(self, other):
        if self.behave == other.behave and self.behave == 1:
            self.candy += 2
            other.candy += 2
        elif self.behave < other.behave:
            self.candy += 3
            other.candy -= 1
        elif self.behave > other.behave:
            self.candy -= 1
            other.candy += 3


class Cheater(Player):
    def __init__(self):
        super().__init__()
        self.name = 'cheater'
        self.prev = 0
        self.behave = 0  # 0-cheat (always)

    def update_state(self):
        self.prev = 0
        self.behave = 0
        self.candy = 0

    def update_behave(self, other):
        # always cheats
        if other.prev == 0:
            self.behave = 0
        else:
            self.behave = 0


class Cooperative(Player):
    def __init__(self):
        super().__init__()
        self.name = 'cooperative'
        self.prev = 1
        self.behave = 1  # 1-cooperate (always)

    def update_state(self):
        self.prev = 1
        self.behave = 1
        self.candy = 0

    def update_behave(self, other):
        # always cooperates
        if other.prev == 0:
            self.behave = 1
        else:
            self.behave = 1


class Copycat(Player):
    def __init__(self):
        super().__init__()
        self.name = 'copycat'
        self.prev = 1  # 1-cooperate (starts with cooperating)
        self.behave = 1  # 1-cooperate (starts with cooperating)

    def update_state(self):
        self.prev = 1
        self.behave = 1
        self.candy = 0

    def update_behave(self, other):
        # starts with cooperating, but then just repeats whatever the other guy is doing
        if other.prev == 0:
            self.behave = 0
        else:
            self.behave = 1


class Grudger(Player):
    def __init__(self):
        super().__init__()
        self.name = 'grudger'
        self.prev = 1
        self.behave = 1  # 1-cooperate (starts with cooperating)
        self.flag = 1

    def update_state(self):
        self.prev = 1
        self.behave = 1
        self.candy = 0
        self.flag = 1

    def update_behave(self, other):
        # starts by always cooperating, but switches to Cheater forever if another guy cheats even once
        if other.prev == 0:
            self.behave = 0
            self.flag = 0
        elif other.prev == 1 and self.flag == 1:
            self.behave = 1
        elif other.prev == 1 and self.flag == 0:
            self.behave = 0


class Detective(Player):
    def __init__(self):
        super().__init__()
        self.name = 'detective'
        self.prev = 1
        self.behave = 1  # 1-cooperate (First four times goes with [Cooperate, Cheat, Cooperate, Cooperate])
        self.step = 0  # counter of player's steps
        self.switch = 1  # 2 - switches into a Copycat, 0 - switches into Cheater

    def update_state(self):
        self.prev = 1
        self.behave = 1
        self.candy = 0
        self.step = 0
        self.switch = 1

    def record_behave(self):
        self.prev = self.behave
        self.step += 1

    def update_switch(self, other):
        # switch behavior after four steps
        if other.prev == 0 and self.step < 4:
            self.switch = 2  # Copycat
        elif other.prev == 1 and self.step < 4 and self.switch != 2:
            self.switch = 0  # Cheater

    def update_behave(self, other):
        # first four times goes with [Cooperate, Cheat, Cooperate, Cooperate]
        if self.step == 1:  # after first step (second step)
            self.behave = 0
            self.update_switch(other)
        elif self.step == 2 or self.step == 3:
            self.behave = 1
            self.update_switch(other)
        elif self.step >= 4:  # behavior after four steps
            if self.switch == 2 and other.prev == 1:
                self.behave = 1  # Copycat
            else:
                self.behave = 0  # as Cheater or cheat as Copycat after cheating


if __name__ == "__main__":
    game = Game()
    game.all_game()
    game.top3()
    # print("Результат игры:")
    # print(game)