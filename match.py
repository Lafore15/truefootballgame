from team import Team
from player import Player
import random


class Match:
    def __init__(self):
        pass

    def get_match(self, Team):
        self.group = []
        self.match = []
        if type(Team) == list:
            self.group.extend(Team)
        else:
            return 'please, enter teams in list'
        if len(Team) > 2:
            self.match.append(random.choice(self.group))
            self.match.append(random.choice(self.group))
            while self.match[0] == self.match[1]:
                self.match.pop(1)
                self.match.append(random.choice(self.group))
        else:
            self.match.extend(self.group)
        if self.match[0].get_final_score() > self.match[1].get_final_score():
            self.winner = self.match[0]
        elif self.match[0].get_final_score() < self.match[1].get_final_score():
            self.winner = self.match[1]
        else:
            self.winner = 'Draw'
        if self.winner != 'Draw':
            return f'{self.match[0].team} versus {self.match[1].team}', 'WINNER ISSSSS......', self.winner.team
        return f'{self.match[0].team} versus {self.match[1].team}', 'WINNER ISSSSS......', 'Nobody,today without winner'


liga_champions = Match
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

lewa = Player('Lewandowski', 9, 'forward', 95)
muller = Player('Muller', 25, 'midfielder', 94)
davies = Player('Davies', 19, 'cb', 90)
neuer = Player('Neuer', 1, 'goalkeeper', 90)
sule = Player('Sule', 4, 'cb', 84)
ulreich = Player('Ulreich', 26, 'goalkeeper', 80)
kimmich = Player('kimmich', 6, 'midfielder', 95)

bayern = Team('Bayern')
juventus.add_players([paulo, danilo, weston, buffon, leo, carlo, zakaria])

chelsea.add_players([werner, kai, cesar, mendy, silva, kepa, kante])

bayern.add_players([lewa, muller, davies, neuer, sule, ulreich, kimmich])

print(liga_champions.get_match(liga_champions(), [juventus, chelsea, bayern]))
