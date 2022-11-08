n = int(input())
ss = [input() for i in range(n)]
games = []
for i in ss:
    games += i.split(';')
d = set()
for i in range(0, len(games), 2):
    d.add(games[i])
dict_games = {}
for i in d:
    dict_games[i] = games.count(i)
s, dict_win, dict_drow, dict_defeat, dict_score = [], {}, {}, {}, {}
for i in range(0, len(games), 2):
    dict_win[games[i]] = 0
    dict_drow[games[i]] = 0
    dict_defeat[games[i]] = 0
    dict_score[games[i]] = 0
for i in ss:
    i = i.split(';')
    s += [i]
for j in s:
    while 1:
        if int(j[1]) > int(j[3]):
            dict_win[j[0]] += 3
            dict_score[j[0]] += 1
            dict_defeat[j[2]] += 1
        if int(j[3]) > int(j[1]):
            dict_win[j[2]] += 3
            dict_score[j[2]] += 1
            dict_defeat[j[0]] += 1
        if int(j[1]) == int(j[3]):
            dict_win[j[0]] += 1
            dict_win[j[2]] += 1
            dict_drow[j[0]] += 1
            dict_drow[j[2]] += 1
        break
for i in dict_games:
    print(i, end=':')
    print(dict_games[i], dict_score[i], dict_drow[i], dict_defeat[i], dict_win[i])
