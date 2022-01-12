import sys
class League():
 
    def __init__(self,filename) -> None:#initialization of the League class using the __init__ method.
        self.filename = filename#assign the value stored int self.filename to the variable name
        self.teams = self.get_teams()
        self.points = {i:0 for i in self.teams}
        self.goal_diff = {i:0 for i in self.teams}
        self.goal_done = {i:0 for i in self.teams}
        self.goal_conceded = {i:0 for i in self.teams}
        self.matches_played = {i:0 for i in self.teams}
        self.matches_won = {i:0 for i in self.teams}
        self.matches_lost = {i:0 for i in self.teams}
        self.matches_draw = {i:0 for i in self.teams}
 
    def goal_differnce(self):
        for i in self.teams:
            self.goal_diff[i] = self.goal_done[i] - self.goal_conceded[i]
 
    def get_teams(self):
        teams = []
        with open(self.filename) as f:
            for line in f:
                line = line.strip().split(',')
                teams.append(line[0])
                teams.append(line[2])
            teams = list(set(teams))
        return teams
 
    def counter(self):
        with open(self.filename) as f:
            for line in f:
                line = line.strip().split(',')
                t1 = line[0]
                t2 = line[2]
                g1 = int(line[1])
                g2 = int(line[3])
                self.goal_done[t1] += g1
                self.goal_done[t2] += g2
                self.goal_conceded[t1] += g2
                self.goal_conceded[t2] += g1
                self.matches_played[t1] += 1
                self.matches_played[t2] += 1
                if g1 > g2:
                    self.points[t1] += 3
                    self.matches_won[t1] += 1
                    self.matches_lost[t2] += 1
                elif g1 < g2:
                    self.points[t2] += 3
                    self.matches_won[t2] += 1
                    self.matches_lost[t1] += 1
                else:
                    self.points[t1] += 1
                    self.points[t2] += 1
                    self.matches_draw[t1] += 1
                    self.matches_draw[t2] += 1
        self.goal_differnce()
 
euro = League('game.csv')
euro.counter()
 
li = []
for i in euro.teams:
    li.append((i,euro.points[i],euro.goal_diff[i]))
li.sort(key=lambda x: (x[1], x[2]),reverse=True)
ranked_list = [i[0] for i in li]
 
try:
    print(f"{sys.argv[1]}")
    print("="*len(sys.argv[1]))
except IndexError:
    pass
 
print("\t\tP\tW\tD\tL\tF\tA\tDiff\tPts")
for n,i in enumerate(ranked_list):
    space = " "*(10-len(i))
    print(f"{i}{space}\t{euro.matches_played[i]}\t{euro.matches_won[i]}\t{euro.matches_draw[i]}\t{euro.matches_lost[i]}\t{euro.goal_done[i]}\t{euro.goal_conceded[i]}\t{euro.goal_diff[i]}\t{euro.points[i]}")