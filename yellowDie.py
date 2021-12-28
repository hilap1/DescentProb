import die_face


class YellowDie:

    def __init__(self):
        f1 = die_face.DieFace(1, 0, 1)
        f2 = die_face.DieFace(2, 0, 1)
        f3 = die_face.DieFace(1, 1, 0)
        f4 = die_face.DieFace(0, 1, 1)
        f5 = die_face.DieFace(0, 0, 2)
        f6 = die_face.DieFace(0, 1, 2)
        self.faces = [f1, f2, f3, f4, f5, f6]

    def to_string(self):
        for f in self.faces:
          print(f.to_string())