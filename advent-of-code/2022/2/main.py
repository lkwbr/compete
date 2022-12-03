def part_1():
    # (r)ock, (p)aper, (s)cissors
    tx = {
        'a': 'r',
        'x': 'r',
        'b': 'p',
        'y': 'p',
        'c': 's',
        'z': 's'
    }
    play_scores = {
        # first plays
        'r': 1, 'p': 2, 's': 3, 
        # draws
        'rr': 3, 'pp': 3, 'ss': 3,
        # wins
        'rs': 6, 'pr': 6, 'sp': 6,
        # losses
        'sr': 0, 'rp': 0, 'ps': 0,
    }
    total_score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            opp, you = [tx[x.lower()] for x in line.split()]
            round_score = play_scores[you] + play_scores[you + opp]
            total_score += round_score
    return total_score


def part_2():
    # (r)ock, (p)aper, (s)cissors
    tx = {
        'a': 'r',
        'b': 'p',
        'c': 's',
        # ending: x = lose, y = draw, z = win 
        'x': 0,
        'y': 3,
        'z': 6,
    }
    # plays and their scores; when two characters, the score is associated with
    # the play of the left character
    play_scores = {
        # first plays
        'r': 1, 'p': 2, 's': 3, 
        # draws
        'rr': 3, 'pp': 3, 'ss': 3,
        # wins
        'rs': 6, 'pr': 6, 'sp': 6,
        # losses
        'sr': 0, 'rp': 0, 'ps': 0,
    }
    # scores associated with a certain play
    score_plays = {}
    for play, score in play_scores.items():
        score_plays[score] = score_plays.get(score, []) + [play] 
    total_score = 0
    with open('input.txt') as f:
        for line in f.readlines():
            opp, your_score = [tx[x.lower()] for x in line.split()]
            your_play = [
                plays[0] for plays in score_plays[your_score] 
                if len(plays) == 2 and plays[1] == opp
            ].pop()
            round_score = play_scores[your_play] + play_scores[your_play + opp]
            total_score += round_score
    return total_score


if __name__ == '__main__':
    x = part_2()
    print('x =', x)