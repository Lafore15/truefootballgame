from player import Player


class Team:

    def __init__(self, team):
        self.team = team
        self.sorted_by_position = {'goalkeeper': [], 'cb': [], 'midfielder': [], 'forward': []}
        self.roster = []
        self.sorted_by_rating = []

    def add_players(self, Player):
        if type(Player) == list:
            self.roster.extend(Player)
        else:
            self.roster.append(Player)
        for i in self.roster:
            self.sorted_by_position[i.position].append(i)
        [self.sorted_by_rating.extend(i) for i in self.sorted_by_position.values()]
        for i in range(len(self.sorted_by_rating)):
            for j in range(len(self.sorted_by_rating) - 1):
                if self.sorted_by_rating[j].default_score > self.sorted_by_rating[i].default_score and self.sorted_by_rating[j].position == \
                        self.sorted_by_rating[i].position:
                    self.sorted_by_rating[j], self.sorted_by_rating[i] = self.sorted_by_rating[i], self.sorted_by_rating[j]

    def get_roster(self):
        return [i.surname for i in self.sorted_by_rating]

    def get_final_score(self):
        if len(self.roster) == 0 :
            return 'You forgot add players'
        return sum([i.default_score for i in self.roster])

