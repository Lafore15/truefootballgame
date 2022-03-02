from player import Player


class Team:

    def __init__(self, team):
        self.team = team

    def add_players(self, Player):
        self.roster = []
        if type(Player) == list:
            self.roster.extend(Player)
        else:
            self.roster.append(Player)
        j = 0
        for i in range(j, len(self.roster)):
            if self.roster[i].position == 'goalkeeper':
                self.roster[i], self.roster[j] = self.roster[j], self.roster[i]
                j += 1
        for i in range(j, len(self.roster)):
            if self.roster[i].position == 'cb':
                self.roster[i], self.roster[j] = self.roster[j], self.roster[i]
                j += 1
        for i in range(j, len(self.roster)):
            if self.roster[i].position == 'midfielder':
                self.roster[i], self.roster[j] = self.roster[j], self.roster[i]
                j += 1
        for i in range(j, len(self.roster)):
            if self.roster[i].position == 'forward':
                self.roster[i], self.roster[j] = self.roster[j], self.roster[i]
                j += 1
        j = 0
        for i in range(len(self.roster)):
            for j in range(len(self.roster)):
                if self.roster[j].default_score > self.roster[i].default_score and self.roster[j].position == self.roster[i].position:
                    self.roster[j], self.roster[i] = self.roster[i], self.roster[j]

    def get_roster(self):
        return [i.surname for i in self.roster]

    def get_final_score(self):
        return sum([i.default_score for i in self.roster])


paulo = Player('paulo', 10, 'forward', 85)
weston = Player('Weston', 14, 'midfielder', 84)
danilo = Player('Danilo', 13, 'cb', 90)
buffon = Player('Buffon', 1, 'goalkeeper', 100)
leo = Player('Leonardo', 19, 'cb', 87)
carlo = Player('Carlo', 99, 'goalkeeper', 99)
zakaria = Player('Zakaria', 27, 'midfielder', 83)

juventus = Team('Juventus')

werner = Player('Werner', 11, 'forward', 85)
kai = Player('Havertz', 29, 'midfielder', 87)
cesar = Player('Azpilicueta', 28, 'cb', 95)
mendy = Player('Mendy', 16, 'goalkeeper', 90)
silva = Player('Silva', 6, 'cb', 95)
kepa = Player('Kepa', 1, 'goalkeeper', 85)
kante = Player('Kante', 7, 'midfielder', 99)

chelsea = Team('Chelsea')

lewa = Player('Lewandowski', 9, 'forward', 93)
muller = Player('Muller', 25, 'midfielder', 94)
davies = Player('Davies', 19, 'cb', 90)
neuer = Player('Neuer', 1, 'goalkeeper', 90)
sule = Player('Sule', 4, 'cb', 84)
ulreich = Player('Ulreich', 26, 'goalkeeper', 80)
kimmich = Player('kimmich', 6, 'midfielder', 95)

bayern = Team('Bayern')
juventus.add_players([paulo, danilo, weston, buffon, leo, carlo, zakaria])
juventus.get_final_score()
chelsea.add_players([werner, kai, cesar, mendy, silva, kepa, kante])
chelsea.get_final_score()
bayern.add_players([lewa, muller, davies, neuer, sule, ulreich, kimmich])
bayern.get_final_score()
