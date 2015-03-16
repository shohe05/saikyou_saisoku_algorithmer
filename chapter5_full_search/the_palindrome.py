class ThePalindrome:
    def find(self, s):
        for i in range(-1, -1 * (len(s) + 1), -1):
            if not s[i:] in s[::-1]:
                return len(s) + len(s) + i + 1
        return len(s)

if __name__ == '__main__':
    the_palindrome = ThePalindrome()
    print(the_palindrome.find('abdfhdyrbdbsdfghjkllkjhgfds'))
