class Cryptography:
    def encrypt(self, numbers):
        products = []
        for i in range(len(numbers)):
            products.append((numbers[i] + 1) * self.array_product(numbers[0:i] + numbers[i+1:]))
        return max(products)

    def array_product(self, array):
        i = 1
        for a in array:
            i *= a
        return i

if __name__ == '__main__':
    cryptography = Cryptography()
    numbers = [1, 3, 2, 1, 1, 3]
    print(cryptography.encrypt(numbers))
