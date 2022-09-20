import fractions
from itertools import count
from random import randint
import sys


class Research:
    def __init__(self, path):
        self.path = path
        self.calculations = self.Calculations(self.file_reader())
        self.analytics = self.Analytics(self.file_reader())
    
    def file_reader(self, has_header=True):
        with open(self.path, 'r') as file:
            rows = file.readlines()
        if has_header == True:
            header = rows[0].split(',')
        if len(header) != 2:
            raise Exception('header has to have precisely 2 strings')
        rows = rows[1:]
        if len(rows) == 0:
            raise Exception('file has to have at least 2 rows')
        res = []
        for row in rows:
            row = row.strip()
            if row != '0,1' and row != '1,0':
                raise Exception('Incorrect file')
            res.append([int(n) for n in row.split(',')])
        return res

    class Calculations:
        def __init__(self, data):
            self.data = data

        def counts(self):
            return [sum([elem[0] for elem in self.data]), sum([elem[1] for elem in self.data])]

        def fractions(self, head, tail):
            return [head / (head + tail) * 100, tail / (head + tail) * 100]

    class Analytics(Calculations):
        def __init__(self, data):
            super().__init__(data)

        def predict_random(self, n):
            res = []
            for i in range(n):
                tmp = randint(0, 1)
                res.append([tmp, (tmp + 1) % 2])
            return res

        def predict_last(self):
            return self.data[-1]


if __name__ == "__main__":
    if len(sys.argv) == 2:
        research = Research(sys.argv[1])
        data = research.file_reader()
        print(data)
        counts = research.calculations.counts()
        print(counts[0], counts[1])
        fractions = research.calculations.fractions(counts[0], counts[1])
        print(fractions[0], fractions[1])
        random_predict = research.analytics.predict_random(3)
        print(random_predict)
        last_predict = research.analytics.predict_last()
        print(last_predict)
