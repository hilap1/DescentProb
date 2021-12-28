import die_face
import yellowDie
import blueDie
import greenDie
import redDie
# from abc import ABC,abstractmethod


class Die:

    def factory(self, color):
        localizers = {
            "yellow": yellowDie.YellowDie,
            "blue": blueDie.BlueDie,
            "green": greenDie.GreenDie,
            "red": redDie.RedDie
        }
        return localizers[color]()


    # def to_string(self):
    #     for f in self.faces:
    #       print(f.to_string())
