class KiwiJuiceEasy:
    def the_pouring(self, capacities, bottles, from_id, to_id):
        for i in range(len(from_id)):
            bottles[from_id[i]], bottles[to_id[i]] = self.pour_once({'capacity': capacities[from_id[i]], 'quantity': bottles[from_id[i]]}, {'capacity': capacities[to_id[i]], 'quantity': bottles[to_id[i]]})

        return bottles

    # from: 入れる側, to: 入れられる側
    # _bottle: {capacity: '入る量', quantity: '入ってる量'}
    def pour_once(self, from_bottle, to_bottle):
        to_bottle['quantity'] += from_bottle['quantity']
        if to_bottle['quantity'] > to_bottle['capacity']:
            from_bottle['quantity'] = to_bottle['quantity'] - to_bottle['capacity']
            to_bottle['quantity'] = to_bottle['capacity']
        else:
            from_bottle['quantity'] = 0

        return [from_bottle['quantity'], to_bottle['quantity']]

if __name__ == "__main__":
    kiwi = KiwiJuiceEasy()
    capacities = [700000, 800000, 900000, 1000000]
    bottles = [478478, 468478, 478478, 468478]
    from_id = [2, 3, 2, 0, 1]
    to_id = [0, 1, 1, 3, 2]
    print(kiwi.the_pouring(capacities, bottles, from_id, to_id))
