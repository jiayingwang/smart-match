from collections import Counter

class SimonWhite:

    def similarity(self, x, y):
        if not x and not y:
            return 1.0
        if not x or not y:
            return 0.0

        s_freq = Counter(x)
        t_freq = Counter(y)

        intersection = s_freq & t_freq
        intersection_size = sum(intersection.values())

        return 2 * intersection_size / (len(x) + len(y))

    def dissimilarity(self, a, b):
        return 1 - self.similarity(a, b)

    def __repr__(self):
        return 'SimonWhite'