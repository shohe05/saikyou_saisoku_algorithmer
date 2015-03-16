class InterestingDigits:
    def digit(self, base):
        answers = []
        for i in range(2, base):
            flag = True
            for j in range(1, base):
                for k in range(1, base):
                    for l in range(1, base):
                        if (((j*base*base + k*base + l) % i == 0) and ((j + k + l) % i != 0)):
                            flag = False
                            break
                    if(not flag):
                        break
                if(not flag):
                    break
            if(flag):
                answers.append(i)
        return answers

if __name__ == '__main__':
    interesting_digits = InterestingDigits()
    print(interesting_digits.digit(26))
