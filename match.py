
import random


class Match:
    def __init__(self):
        self.group = []
        self.match = []
        self.winner = ''
        self.ratings = []

    def get_match(self, teams, stadium='neutral'):
        self.winner = ''
        self.group.clear()
        self.match.clear()
        if type(teams) == list:
            self.group.extend(teams)
        else:
            return 'please, enter teams in list'
        if len(teams) > 2:
            self.match.append(random.choice(self.group))
            self.match.append(random.choice(self.group))
            while self.match[0] == self.match[1]:
                self.match.pop(1)
                self.match.append(random.choice(self.group))
        else:
            self.match.extend(self.group)
        first_score = self.match[0].get_final_score()
        second_score = self.match[1].get_final_score()
        if stadium[0] == 'h':
            first_score += 50
        elif stadium[0] == 'a':
            second_score += 50
        if random.randint(0, 101) < 91 and first_score > second_score:
            self.winner = self.match[0]
        elif random.randint(0, 101) < 91 and first_score < second_score:
            self.winner = self.match[1]
        elif random.randint(0, 101) > 91 and first_score < second_score:
            self.winner = self.match[1]
        elif random.randint(0, 101) > 91 and first_score > second_score:
            self.winner = self.match[0]
        elif random.randint(0, 101) == 50:
            self.winner = 'Draw'
        if self.winner == 'Draw':
            return f'{self.match[0].team} versus {self.match[1].team}', 'Draw'
        return f'{self.match[0].team} versus {self.match[1].team}', 'WINNER IS...', self.winner.team

    def get_winner(self):
        return self.winner



