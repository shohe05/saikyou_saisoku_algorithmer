import itertools
class CrazyBot:
    PROBABILITIES = []
    def get_probability(self, n, east, west, south, north):
        CrazyBot.PROBABILITIES = [north / 100, south / 100, east / 100, west / 100]
        return self.move_recursive(n, [0, 0], [])

    def move_recursive(self, n, point, footprints, sum_probability = 1):
        if point in footprints:
            return 0
        if n == 0: return sum_probability
        probability = 0
        for i in [0, 1, 2, 3]:
            probability += self.move_recursive(n - 1, self.move(point, i), self.my_append(footprints, point), sum_probability * self.PROBABILITIES[i])
        return probability

    def move(self, location, direction):
        l = list(location)
        if direction == 0: l[1] += 1
        elif direction == 1: l[1] -= 1
        elif direction == 2: l[0] -= 1
        elif direction == 3: l[0] += 1
        return l

    def my_append(self, array, e):
        a = list(array)
        a.append(e)
        return a

if __name__ == '__main__':
    crazy_bot = CrazyBot()
    print(crazy_bot.get_probability(14, 25, 25, 25, 25))
