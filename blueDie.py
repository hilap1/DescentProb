import die_face


class BlueDie:

    def __init__(self):
        f1 = die_face.DieFace(0, 0, 0)
        f2 = die_face.DieFace(2, 1, 2)
        f3 = die_face.DieFace(3, 0, 2)
        f4 = die_face.DieFace(4, 0, 2)
        f5 = die_face.DieFace(5, 0, 1)
        f6 = die_face.DieFace(6, 1, 1)
        self.faces = [f1, f2, f3, f4, f5, f6]

    def to_string(self):
        for f in self.faces:
          print(f.to_string())