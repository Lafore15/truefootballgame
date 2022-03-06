from match import Match
from team import Team
from player import Player
import input_instances as ip
import random


class Tournament:
    def __init__(self):
        self.buckets = {'first bucket': [], 'second bucket': []}
        self.groups = {'Group A': [], 'Group B': []}

    def create_groups(self, Team):
        self.buckets['first bucket'] = Team[:4]
        self.buckets['second bucket'] = Team[4:]
        first_bucket = self.buckets['first bucket']
        second_bucket = self.buckets['second bucket']
        for i in range(0,3,2) :
            self.groups['Group A'].append(random.choice(first_bucket))
            first_bucket.remove(self.groups['Group A'][i])
            self.groups['Group A'].append(random.choice(second_bucket))
            second_bucket.remove(self.groups['Group A'][i+1])
        self.groups['Group B'] = first_bucket + second_bucket
        return [i.team for i in self.groups['Group A']], [i.team for i in self.groups['Group B']]


liga_champions = Tournament
print(liga_champions.create_groups(liga_champions(),[ip.barca, ip.juventus, ip.chelsea, ip.man_united, ip.inter, ip.bayern, ip.real,ip.liver]))

