from player import Player
class Team:

    def __init__(self, team):
        self.team = team
        self.sorted_by_position = self.sbp = {'goalkeeper': [], 'cb': [], 'midfielder': [], 'forward': []}
        self.roster = []
        self.sorted_by_rating = self.sbr = []

    def add_players(self, players):
        self.roster.clear()
        if type(players) == list:
            self.roster.extend(players)
        else:
            self.roster.append(players)
        for i in self.roster:
            self.sbp[i.position].append(i)
        [self.sbr.extend(i) for i in self.sbp.values()]
        '''def quick_sort(s):
            if len(s) <= 1:
                return s
            elem = s[0].default_score
            left = list(filter(lambda x: x.default_score < elem, s))
            center = [i for i in s if i.default_score == elem]
            right = list(filter(lambda x: x.default_score > elem, s))
            return quick_sort(left) + center + quick_sort(right)'''
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


