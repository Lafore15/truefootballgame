from player import Player


class Team:

    def __init__(self, team):
        self.team = team
        self.sorted_by_position = self.sbp = {'goalkeeper': [], 'cb': [], 'midfielder': [], 'forward': []}
        self.roster = []
        self.sorted_by_rating = self.sbr = []
        self.injured = None

    def __repr__(self):
        return f'{self.team}'

    def __str__(self):
        return f'{self.team}'

    def add_players(self, players):
        self.roster.clear()
        if type(players) == list:
            self.roster.extend(players)
        else:
            self.roster.append(players)
        for i in self.roster:
            self.sbp[i.position].append(i)
        [self.sbr.extend(i) for i in self.sbp.values()]
        for i in range(len(self.sbr)):
            for j in range(len(self.sbr) - 1):
                if self.sbr[j].default_score > self.sbr[i].default_score and self.sbr[j].position == self.sbr[i].position:
                    self.sbr[j], self.sbr[i] = self.sbr[i], self.sbr[j]

    def get_roster(self):
        return [i.surname for i in self.sbr]

    def get_final_score(self):
        if len(self.roster) == 0:
            return 'You forgot add players'
        return sum([i.default_score for i in self.roster])
