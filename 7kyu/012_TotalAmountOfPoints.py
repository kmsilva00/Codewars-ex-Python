#if x > y: 3 points (win)
#if x < y: 0 points (loss)
#if x = y: 1 point (tie)

a = (['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3'])

def points(games):
    score = 0
    for i in games:
        t1,t2 = i.split(":")
        if t1 > t2:
            score += 3
        elif t1 < t2:
            score += 0
        else: 
            score += 1
    return score