import die_face


class GreenDie:
    faces = []
    def __init__(self):
        f1 = die_face.DieFace(1, 0, 1)
        f2 = die_face.DieFace(0, 0, 1)
        f3 = die_face.DieFace(1, 1, 0)
        f4 = die_face.DieFace(0, 1, 0)
        f5 = die_face.DieFace(0, 1, 1)
        f6 = die_face.DieFace(1, 1, 1)
        self.faces = [f1, f2, f3, f4, f5, f6]

    def __str__(self):
        res = ''
        for f in self.faces:
            res = res + str(f) + "\n"
        return res