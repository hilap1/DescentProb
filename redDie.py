import die_face


class RedDie:
    faces = []
    def __init__(self):
        f1 = die_face.DieFace(0, 0, 1)
        f2 = die_face.DieFace(0, 0, 2)
        f3 = die_face.DieFace(0, 0, 3)
        f4 = die_face.DieFace(0, 1, 3)
        self.faces = [f1, f2, f2, f2, f3, f4]

    def __str__(self):
        res = ''
        for f in self.faces:
            res = res + str(f) + "\n"
        return res