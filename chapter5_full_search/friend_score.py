class FriendScore:
    def highest_score(self, friends):
        maxi = 0
        for i in range(len(friends)):
            my_friends = []
            for j in range(len(friends[i])):
                if friends[i][j] == 'Y':
                    my_friends.append(j)
            mm = list(my_friends)
            for k in my_friends:
                for l in range(len(friends[k])):
                    if friends[k][l] == 'Y' and l != i and l not in my_friends:
                        mm.append(l)
            maxi = max(maxi, len(mm))
        return maxi

if __name__ == '__main__':
    friend_score = FriendScore()
    # friends = ['NYNNN', 'YNYNN', 'NYNYN', 'NNYNY', 'NNNYN']
    friends = ['NNNNYNNNNN', 'NNNNYNYYNN', 'NNNYYYNNNN', 'NNYNNNNNNN',
              'YYYNNNNNNY', 'NNYNNNNNYN', 'NYNNNNNYNN', 'NYNNNNYNNN',
              'NNNNNYNNNN', 'NNNNYNNNNN']
    print(friend_score.highest_score(friends))
