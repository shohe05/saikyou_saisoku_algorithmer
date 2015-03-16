class InterestingParty:
    def best_invitation(self, first, second):
        all_hobbies = first + second
        hobby_popularity = {}
        for hobby in all_hobbies:
            hobby_popularity[hobby] = hobby_popularity.get(hobby, 0) + 1
        return max(hobby_popularity.values())

if __name__ == "__main__":
    interesting_party = InterestingParty()
    first = ['sn', 'pr', 'co', 'mo']
    second = ['a', 'b', 'c', 'd']
    print(interesting_party.best_invitation(first, second))
