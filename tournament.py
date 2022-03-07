from match import Match
import input_instances as ip
import random
import copy


class Tournament:
    def __init__(self):
        self.buckets = {'first bucket': [], 'second bucket': []}
        self.groups = {'Group A': [], 'Group B': []}
        self.quarterfinalists1 = []
        self.quarterfinalists2 = []
        self.semifinalists = []
        self.champion = []

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

    def create_playoff(self):
        a_group = copy.deepcopy(self.groups['Group A'])
        b_group = copy.deepcopy(self.groups['Group B'])
        already_played = []
        semifinalists = []
        quarterfinalists1 = []
        quarterfinalists2 = []
        for i in range(4):
            match1 = Match()
            already_played.clear()
            match1.get_match([random.choice(a_group), random.choice(b_group)])
            already_played.extend(match1.group)
            a_group.remove(already_played[0])
            b_group.remove(already_played[1])
            if i % 2 == 0:
                quarterfinalists1.append(match1.winner)
            else:
                quarterfinalists2.append(match1.winner)
            del match1
        self.quarterfinalists1 = copy.deepcopy(quarterfinalists1)
        self.quarterfinalists2 = copy.deepcopy(quarterfinalists2)
        for _ in range(2):
            match1 = Match()
            already_played.clear()
            match1.get_match([random.choice(quarterfinalists1), random.choice(quarterfinalists2)])
            already_played.extend(match1.group)
            quarterfinalists1.remove(already_played[0])
            quarterfinalists2.remove(already_played[1])
            semifinalists.append(match1.winner)
            del match1
        grand_final = Match()
        grand_final.get_match(semifinalists)
        return grand_final.get_winner().team, [i.team  for i in semifinalists], [i.team for i in self.quarterfinalists1], [i.team for i in self.quarterfinalists2]



