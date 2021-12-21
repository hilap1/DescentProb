import die_face


class Die:
    def __init__(self, color):
        self.color = color
        if color == 'red':
            f1 = die_face.DieFace(0, 0, 1)
            f2 = die_face.DieFace(0, 0, 2)
            f3 = die_face.DieFace(0, 0, 3)
            f4 = die_face.DieFace(0, 1, 3)
            self.faces = [f1, f2, f2, f2, f3, f4]
        if color == 'blue':
            f1 = die_face.DieFace(0, 0, 0)
            f2 = die_face.DieFace(2, 1, 2)
            f3 = die_face.DieFace(3, 0, 2)
            f4 = die_face.DieFace(4, 0, 2)
            f5 = die_face.DieFace(5, 0, 1)
            f6 = die_face.DieFace(6, 1, 1)
            self.faces = [f1, f2, f3, f4, f5, f6]
        if color == 'green':
            f1 = die_face.DieFace(1, 0, 1)
            f2 = die_face.DieFace(0, 0, 1)
            f3 = die_face.DieFace(1, 1, 0)
            f4 = die_face.DieFace(0, 1, 0)
            f5 = die_face.DieFace(0, 1, 1)
            f6 = die_face.DieFace(1, 1, 1)
            self.faces = [f1, f2, f3, f4, f5, f6]
        if color == 'yellow':
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
