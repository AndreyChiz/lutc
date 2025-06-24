class SContains:
    def __init__(self, data: list):
        self.data =data

    def __contains__(self, x):
        return x in self.data
