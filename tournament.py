from match import Match
import input_instances as ip
import random
import copy


class Tournament:
    def __init__(self):
        self.buckets = {'first bucket': [], 'second bucket': []}
        self.groups = {'Group A': [], 'Group B': []}
        self.history_of_games_a = []
        self.history_of_games_b = []
        self.points_a = {}
        self.points_b = {}

    def create_groups(self, teams):
        self.buckets['first bucket'] = copy.deepcopy(teams[:4])
        self.buckets['second bucket'] = copy.deepcopy(teams[4:])
        first_bucket = copy.deepcopy(self.buckets['first bucket'])
        second_bucket = copy.deepcopy(self.buckets['second bucket'])
        for i in range(0, 3, 2):
            self.groups['Group A'].append(random.choice(first_bucket))
            first_bucket.remove(self.groups['Group A'][i])
            self.groups['Group A'].append(random.choice(second_bucket))
            second_bucket.remove(self.groups['Group A'][i + 1])
        self.groups['Group B'] = first_bucket + second_bucket

    def get_groups(self):
        return [i.team for i in self.groups['Group A']], [i.team for i in self.groups['Group B']]

    def play_groups(self):
        self.points_a = {}
        for team in self.groups['Group A']:
            self.points_a[team] = 0
        for i in range(len(self.groups['Group A']) * 2):
            match = Match()
            if i < len(self.groups['Group A']):
                if i + 1 == len(self.groups['Group A']):
                    match.get_match([self.groups['Group A'][i], self.groups['Group A'][0]], stadium='h')
                    self.history_of_games_a.append(match.result)
                    if match.get_winner() is None:
                        self.points_a[match.match[0]] += 1
                        self.points_a[match.match[1]] += 1
                    else:
                        self.points_a[match.get_winner()] += 3
                else:
                    match.get_match([self.groups['Group A'][i], self.groups['Group A'][i + 1]], stadium='h')
                    self.history_of_games_a.append(match.result)
                    if match.get_winner() is None:
                        self.points_a[match.match[0]] += 1
                        self.points_a[match.match[1]] += 1
                    else:
                        self.points_a[match.get_winner()] += 3
                del match
            else:
                if i-len(self.groups['Group A']) - 1 + 1 == len(self.groups['Group A']):
                    match.get_match([self.groups['Group A'][i-len(self.groups['Group A']) - 1], self.groups['Group A'][0]], stadium='a')
                    self.history_of_games_a.append(match.result)
                    if match.get_winner() is None:
                        self.points_a[match.match[0]] += 1
                        self.points_a[match.match[1]] += 1
                    else:
                        self.points_a[match.get_winner()] += 3
                else:
                    match.get_match([self.groups['Group A'][i-len(self.groups['Group A']) - 1], self.groups['Group A'][i - len(self.groups['Group A'])]], stadium='a')
                    self.history_of_games_a.append(match.result)
                    if match.get_winner() is None:
                        self.points_a[match.match[0]] += 1
                        self.points_a[match.match[1]] += 1
                    else:
                        self.points_a[match.get_winner()] += 3
                del match
        for i in range(len(self.groups['Group A'])):
            match = Match()
            if i + 2 >= len(self.groups['Group A']):
                match.get_match([self.groups['Group A'][i], self.groups['Group A'][i + 2 - len(self.groups['Group A'])]], stadium='h')
                self.history_of_games_a.append(match.result)
                if match.get_winner() is None:
                    self.points_a[match.match[0]] += 1
                    self.points_a[match.match[1]] += 1
                else:
                    self.points_a[match.get_winner()] += 3
            else:
                match.get_match([self.groups['Group A'][i], self.groups['Group A'][i + 2]], stadium='h')
                self.history_of_games_a.append(match.result)
                if match.get_winner() is None:
                    self.points_a[match.match[0]] += 1
                    self.points_a[match.match[1]] += 1
                else:
                    self.points_a[match.get_winner()] += 3
            del match
        self.points_b = {}
        for team in self.groups['Group B']:
            self.points_b[team] = 0
        for i in range(len(self.groups['Group B']) * 2):
            match = Match()
            if i < len(self.groups['Group B']):
                if i + 1 == len(self.groups['Group B']):
                    match.get_match([self.groups['Group B'][i], self.groups['Group B'][0]], stadium='h')
                    self.history_of_games_b.append(match.result)
                    if match.get_winner() is None:
                        self.points_b[match.match[0]] += 1
                        self.points_b[match.match[1]] += 1
                    else:
                        self.points_b[match.get_winner()] += 3
                else:
                    match.get_match([self.groups['Group B'][i], self.groups['Group B'][i + 1]], stadium='h')
                    self.history_of_games_b.append(match.result)
                    if match.get_winner() is None:
                        self.points_b[match.match[0]] += 1
                        self.points_b[match.match[1]] += 1
                    else:
                        self.points_b[match.get_winner()] += 3
                del match
            else:
                if i-len(self.groups['Group B']) - 1 + 1 == len(self.groups['Group B']):
                    match.get_match([self.groups['Group B'][i-len(self.groups['Group B']) - 1], self.groups['Group B'][0]], stadium='a')
                    self.history_of_games_b.append(match.result)
                    if match.get_winner() is None:
                        self.points_b[match.match[0]] += 1
                        self.points_b[match.match[1]] += 1
                    else:
                        self.points_b[match.get_winner()] += 3
                else:
                    match.get_match([self.groups['Group B'][i-len(self.groups['Group B']) - 1], self.groups['Group B'][i - len(self.groups['Group B'])]], stadium='a')
                    self.history_of_games_b.append(match.result)
                    if match.get_winner() is None:
                        self.points_b[match.match[0]] += 1
                        self.points_b[match.match[1]] += 1
                    else:
                        self.points_b[match.get_winner()] += 3
                del match
        for i in range(len(self.groups['Group B'])):
            match = Match()
            if i + 2 >= len(self.groups['Group B']):
                match.get_match([self.groups['Group B'][i], self.groups['Group B'][i + 2 - len(self.groups['Group B'])]], stadium='h')
                self.history_of_games_b.append(match.result)
                if match.get_winner() is None:
                    self.points_b[match.match[0]] += 1
                    self.points_b[match.match[1]] += 1
                else:
                    self.points_b[match.get_winner()] += 3
            else:
                match.get_match([self.groups['Group B'][i], self.groups['Group B'][i + 2]], stadium='h')
                self.history_of_games_b.append(match.result)
                if match.get_winner() is None:
                    self.points_b[match.match[0]] += 1
                    self.points_b[match.match[1]] += 1
                else:
                    self.points_b[match.get_winner()] += 3
            del match
        self.points_a = {k: v for k, v in sorted(self.points_a.items(), key=lambda item: item[1])}
        self.points_b = {k: v for k, v in sorted(self.points_b.items(), key=lambda item: item[1])}
        return self.points_a, self.points_b

    def create_playoff(self):
        points_a = copy.deepcopy(self.points_a)
        points_b = copy.deepcopy(self.points_a)
        a = list(points_a.keys())
        b = list(points_b.keys())
        f_semi_final = []
        s_semi_final = []
        history_of_playoff_games = []
        grand_final_teams = []
        grand_final = Match()
        if [value for value in points_a.values()].count(max(points_a.values())) == 1:
            f_semi_final.append(a[3])
            del points_a[a[3]]
        elif [value for value in points_a.values()].count(max(points_a.values())) == 2:
            if a[3].get_final_score() > a[2].get_final_score():
                f_semi_final.append(a[3])
                del points_a[a[3]]
            elif a[3].get_final_score() < a[2].get_final_score():
                f_semi_final.append(a[2])
                del points_a[a[2]]
            else:
                f_semi_final.append(random.choice([a[2], a[3]]))
                del points_a[f_semi_final[0]]
        elif [value for value in points_a.values()].count(max(points_a.values())) == 3:
            if max([a[1].get_final_score(), a[2].get_final_score(), a[3].get_final_score()]) == a[1].get_final_score:
                f_semi_final.append(a[1])
                del points_a[a[1]]
            elif max([a[1].get_final_score(), a[2].get_final_score(), a[3].get_final_score()]) == a[2].get_final_score:
                f_semi_final.append(a[2])
                del points_a[a[2]]
            elif max([a[1].get_final_score(), a[2].get_final_score(), a[3].get_final_score()]) == a[3].get_final_score:
                f_semi_final.append(a[3])
                del points_a[a[3]]
            else:
                f_semi_final.append(random.choice([a[1], a[2], a[3]]))
                del points_a[f_semi_final[0]]

        if [value for value in points_b.values()].count(max(points_b.values())) == 1:
            f_semi_final.append(b[3])
            del points_b[b[3]]
        elif [value for value in points_b.values()].count(max(points_b.values())) == 2:
            if b[3].get_final_score() > b[2].get_final_score():
                f_semi_final.append(b[3])
                del points_b[b[3]]
            elif b[3].get_final_score() < b[2].get_final_score():
                f_semi_final.append(b[2])
                del points_b[b[2]]
            else:
                f_semi_final.append(random.choice([b[2], b[3]]))
                del points_b[f_semi_final[1]]
        elif [value for value in points_b.values()].count(max(points_b.values())) == 3:
            if max([b[1].get_final_score(), b[2].get_final_score(), b[3].get_final_score()]) == b[1].get_final_score:
                f_semi_final.append(b[1])
                del points_b[b[1]]
            elif max([b[1].get_final_score(), b[2].get_final_score(), b[3].get_final_score()]) == b[2].get_final_score:
                f_semi_final.append(a[2])
                del points_b[b[2]]
            elif max([b[1].get_final_score(), b[2].get_final_score(), b[3].get_final_score()]) == b[3].get_final_score:
                f_semi_final.append(b[3])
                del points_b[b[3]]
            else:
                f_semi_final.append(random.choice([b[1], b[2], b[3]]))
                del points_b[f_semi_final[1]]

        if [value for value in points_a.values()].count(max(points_a.values())) == 1:
            s_semi_final.append(a[2])
        elif [value for value in points_a.values()].count(max(points_a.values())) == 2:
            if a[2].get_final_score() > a[1].get_final_score():
                s_semi_final.append(a[2])
            elif a[2].get_final_score() < a[1].get_final_score():
                s_semi_final.append(a[1])
            else:
                s_semi_final.append(random.choice([a[1], a[2]]))
        elif [value for value in points_a.values()].count(max(points_a.values())) == 3:
            if max([a[1].get_final_score(), a[2].get_final_score(), a[0].get_final_score()]) == a[0].get_final_score:
                s_semi_final.append(a[0])
            elif max([a[1].get_final_score(), a[2].get_final_score(), a[0].get_final_score()]) == a[1].get_final_score:
                s_semi_final.append(a[1])
            elif max([a[1].get_final_score(), a[2].get_final_score(), a[0].get_final_score()]) == a[2].get_final_score:
                s_semi_final.append(a[2])
            else:
                s_semi_final.append(random.choice([a[0], a[1], a[2]]))

        if [value for value in points_b.values()].count(max(points_b.values())) == 1:
            s_semi_final.append(b[2])
        elif [value for value in points_b.values()].count(max(points_b.values())) == 2:
            if b[2].get_final_score() > b[1].get_final_score():
                s_semi_final.append(b[2])
            elif b[2].get_final_score() < b[1].get_final_score():
                s_semi_final.append(b[1])
            else:
                s_semi_final.append(random.choice([b[1], b[2]]))
        elif [value for value in points_b.values()].count(max(points_b.values())) == 3:
            if max([b[0].get_final_score(), b[1].get_final_score(), b[2].get_final_score()]) == b[0].get_final_score:
                s_semi_final.append(b[0])
            elif max([b[0].get_final_score(), b[1].get_final_score(), b[2].get_final_score()]) == b[1].get_final_score:
                s_semi_final.append(a[1])
            elif max([b[0].get_final_score(), b[1].get_final_score(), b[2].get_final_score()]) == b[2].get_final_score:
                s_semi_final.append(b[2])
            else:
                s_semi_final.append(random.choice([b[0], b[1], b[2]]))

        for i in range(2):
            match = Match()
            match.get_match([f_semi_final[0], s_semi_final[1]])
            history_of_playoff_games.append(match.winner)
            del match
        if history_of_playoff_games[0] != history_of_playoff_games[1]:
            match = Match()
            match.get_match([f_semi_final[0], s_semi_final[1]])
            if match.winner is None:
                match.winner = match.match[0]
            grand_final_teams.append(match.winner)
        else:
            grand_final_teams.append(history_of_playoff_games[0])
        history_of_playoff_games.clear()

        for i in range(2):
            match = Match()
            match.get_match([f_semi_final[1], s_semi_final[0]])
            history_of_playoff_games.append(match.winner)
            del match
        if history_of_playoff_games[0] != history_of_playoff_games[1]:
            match = Match()
            match.get_match([f_semi_final[1], s_semi_final[0]])
            if match.winner is None:
                match.winner = match.match[0]
            grand_final_teams.append(match.winner)
        else:
            grand_final_teams.append(history_of_playoff_games[0])
        grand_final = Match()
        grand_final.get_match(grand_final_teams)
        champion = grand_final.winner
        while champion is None:
            del grand_final
            grand_final = Match()
            team = random.choice(grand_final.match).get_final_score()
            team += 5
            grand_final.get_match(grand_final_teams)
            champion = grand_final.winner
        return f_semi_final, s_semi_final, champion


champions_league = Tournament()
champions_league.create_groups([ip.juventus, ip.bayern, ip.inter, ip.man_united, ip.chelsea, ip.barca, ip.real, ip.liver])
print(champions_league.get_groups())
champions_league.play_groups()
print(champions_league.create_playoff())
