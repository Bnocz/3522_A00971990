class SmurfParade:
    def __init__(self, smurfs):
        self.smurfs = smurfs

    def __len__(self):
        return len(self.smurfs)

    def __contains__(self, smurfs):
        return smurfs in self.smurfs

    def __iter__(self):
        yield from self

    def __getitem__(self, item):
        return self.smurfs[item]

    def count(self, item):
        count = 0
        for item in self.smurfs:
            count += 1
        return count

def main():
    s = SmurfParade(["apple",2,"apple"])
    print(s.count("apple"))


if __name__ == '__main__':
    main()