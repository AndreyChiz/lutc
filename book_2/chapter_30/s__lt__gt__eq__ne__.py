class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other