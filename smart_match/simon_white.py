from collections import Counter

class SimonWhite:

    def similarity(self, a, b):
        if not a and not b:
            return 1
        if not a or not b:
            return 0

        freqA = Counter(a)
        freqB = Counter(b)

        intersection = freqA & freqB
        intersection_size = sum(intersection.values())

        return 2 * intersection_size / (len(a) + len(b))

    def dissimilarity(self, a, b):
        return 1 - self.similarity(a, b)

    def __repr__(self):
        return 'SimonWhite'