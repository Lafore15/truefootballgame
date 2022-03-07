from player import Player
from team import Team
from match import Match

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

depay = Player('Memphis', 9, 'forward', 87)
auba = Player('Pierre', 33, 'forward', 90)
pedri = Player('Pedri', 16, 'midfielder', 91)
gavi = Player('Gavi', 32, 'midfielder', 87)
umtiti = Player('Kakashka', 6, 'cb', 80)
pique = Player('Shakira', 3, 'cb', 99)
stegen = Player('Marl-Andre', 1, 'goalkeeper', 95)

barca = Team('Barcelona')

salah = Player('Mo', 10, 'forward', 95)
firmino = Player('firmino', 9, 'forward', 94)
mane = Player('Mane', 11, 'forward', 96)
trent = Player('Trent', 66, 'cb', 90)
thiago = Player('Thiago', 6, 'midfielder', 87)
allison = Player('Alisson', 1, 'goalkeeper', 90)
dijk = Player('Van', 4, 'cb', 90)

liver = Team('Liverpool')

ronaldo = Player('Ronaldo', 7, 'forward', 1)
bruno = Player('Bruno', 7, 'midfielder', 90)
cavani = Player('Cavani', 9, 'forward', 87)
fred = Player('Fred', 6, 'midfielder', 88)
harry = Player('Harry', 3, 'cb', 85)
de = Player('De Gea', 1, 'goalkeeper', 90)
lindelof = Player('Lindelof', 4, 'forward', 85)

man_united = Team('Manchester United')

dzeko = Player('Edin', 10, 'forward', 90)
lautaro = Player('Martinez', 9, 'forward', 93)
skriniar = Player('Skriniar', 3, 'cb', 90)
hakan = Player('Hakan', 11, 'forward', 92)
barella = Player('Barella', 12, 'midfielder', 96)
handanovic = Player('Handanovic', 1, 'goalkeeper', 95)
vidal = Player('Vidal', 4, 'midfielder', 90)

inter = Team('Inter')

benz = Player('Benz', 9, 'forward', 99)
bale = Player('Bale', 10, 'forward', 85)
kroos = Player('kroos', 8, 'midfielder', 90)
modric = Player('modric', 6, 'midfielder', 91)
militao = Player('Militao', 3, 'cb', 90)
courtua = Player('Courtua', 1, 'goalkeeper', 90)
carvajal = Player('Carvajal', 4, 'cb', 90)

real = Team('Real')

juventus.add_players([paulo, danilo, weston, buffon, leo, carlo, zakaria])

chelsea.add_players([werner, kai, cesar, mendy, silva, kepa, kante])

bayern.add_players([lewa, muller, davies, neuer, sule, ulreich, kimmich])

barca.add_players([depay, umtiti, stegen, pique, gavi, pedri, auba])

real.add_players([kroos, modric, bale, benz, carvajal, militao, courtua])

liver.add_players([thiago, allison, firmino, salah, mane, trent, dijk])

inter.add_players([dzeko, lautaro, hakan, skriniar, handanovic, vidal, barella])

man_united.add_players([ronaldo, harry, lindelof, bruno, cavani, fred, de])

