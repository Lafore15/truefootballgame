from match import Match
import input_instances as ip
import random
import copy


class Tournament:
    def __init__(self):
        self.champion = []
        self.gft = []
        self.buckets = {}
        self.groups = {}
        self.points = {}
        self.all_points = {}
        self.draw = 1
        self.win = 3

    def create_groups(self, teams):
        number_of_teams_in_bucket = ntb = 4
        number_of_teams_in_group = ntg = 4
        number_of_groups = ng = 2
        count = 0
        bucket = 1
        for i in range(len(teams)):
            count += 1
            if count % ntb == 0 and count != len(teams):
                self.buckets[bucket] = teams[count:(i+1+ntb)]
                bucket += 1
            elif count == 1:
                self.buckets[bucket] = teams[:ntb]
                bucket += 1
        buckets = list(copy.deepcopy(self.buckets).values())
        for i in range(ng):
            group_name = 'Group ' + chr(65 + i)
            self.groups[group_name] = []
            for j in range(ntg):
                if j < len(buckets):
                    self.groups[group_name].append(random.choice(buckets[j]))
                    buckets[j].remove(self.groups[group_name][-1])
                else:
                    self.groups[group_name].append(random.choice(buckets[j - len(buckets)]))
                    buckets[j - len(buckets)].remove(self.groups[group_name][-1])
        return self.groups

    def play_groups(self):
        def create_match(group, points, ha):
            if len(points) == 0:
                for i in group:
                    points[i] = 0
            draw = 1
            win = 3
            for i in range(len(group)):
                match = Match()
                if i + 1 == len(group):
                    match.get_match([group[i], group[0]], stadium=ha)
                    if match.get_winner() is None:
                        points[match.match[0]] += draw
                        points[match.match[1]] += draw
                    else:
                        points[match.get_winner()] += win
                else:
                    match.get_match([group[i], group[i + 1]], stadium=ha)
                    if match.get_winner() is None:
                        points[match.match[0]] += draw
                        points[match.match[1]] += draw
                    else:
                        points[match.get_winner()] += win
                del match
            return points

        def create_match_2(group, points):
            draw = 1
            win = 3
            for i in range(len(group)):
                match = Match()
                if i + 2 >= len(group):
                    match.get_match([group[i], group[i + 2 - len(group)]], stadium='a')
                    if match.get_winner() is None:
                        points[match.match[0]] += draw
                        points[match.match[1]] += draw
                    else:
                        points[match.get_winner()] += win
                else:
                    match.get_match([group[i], group[i + 2]], stadium='h')
                    if match.get_winner() is None:
                        points[match.match[0]] += draw
                        points[match.match[1]] += draw
                    else:
                        points[match.get_winner()] += win
                del match
            return points
        for i in self.groups.keys():
            create_match(self.groups[i], self.points, 'h')
            create_match(self.groups[i], self.points, 'a')
            create_match_2(self.groups[i], self.points)
            self.all_points[i] = copy.deepcopy(self.points)
            self.points.clear()
        for i in self.all_points.keys():
            self.all_points[i] = {k: v for k, v in sorted(self.all_points[i].items(), key=lambda item: item[1])}
        return self.all_points

    def create_playoff(self):
        semifinals = []
        history_of_playoff_games = hpg = []
        grand_final_teams = gft = []
        grand_final = Match()

        def playoffs(group):
            teams = list(group.keys())
            amount_of_max_points = amx = [value for value in group.values()].count(max(group.values()))
            scores = [teams[-i].get_final_score() for i in range(1, amx + 1)]
            max_score = max(scores)
            max_score_index = scores.index(max_score)
            if amx == 1:
                semifinals.append(teams[-1])
                del group[teams[-1]]
            else:
                semifinals.append(teams[max_score_index])
                del group[teams[max_score_index]]
            return group
        for i in range(len(self.groups.keys())):
            playoffs(self.all_points['Group A'])
            playoffs(self.all_points['Group B'])

        def final_stage(playoff_stage):
            for i in range(0, len(playoff_stage), 2):
                match = Match()
                match.get_match([playoff_stage[i], playoff_stage[i + 1]])
                history_of_playoff_games.append(match.winner)
                del match
        final_stage(semifinals)
        final_stage(semifinals)
        for i in range(0, len(hpg), 2):
            if hpg[i] != hpg[i+1]:
                match = Match()
                match.get_match([semifinals[i], semifinals[i + 1]])
                if match.winner is None:
                    match.winner = random.choice(match.match)
                grand_final_teams.append(match.winner)
            else:
                grand_final_teams.append(hpg[i])
        hpg.clear()
        grand_final.get_match(gft)
        champion = grand_final.winner
        while champion is None:
            del grand_final
            grand_final = Match()
            team = random.choice(grand_final.match).get_final_score()
            team += 5
            grand_final.get_match(gft)
            champion = grand_final.winner
        self.gft = gft
        self.champion = champion
        return semifinals, grand_final_teams, champion


champions_league = Tournament()
print(champions_league.create_groups([ip.juventus, ip.bayern, ip.inter, ip.man_united, ip.chelsea, ip.barca, ip.real, ip.liver]))
print(champions_league.play_groups())
print(champions_league.create_playoff())
