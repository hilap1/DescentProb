class DieFace:
    def __init__(self, range, surge, hearts):
        self.range = range
        self.surge = surge
        self.hearts = hearts

    def __str__(self):
        return 'range: ' + str(self.range) + ', surge: ' + str(self.surge) + ', hearts: ' + str(self.hearts)
