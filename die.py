import yellowDie
import blueDie
import greenDie
import redDie
# import die_face
# from abc import ABC, abstractmethod


class Die:

    def factory(self, color):
        localizers = {
            "yellow": yellowDie.YellowDie,
            "blue": blueDie.BlueDie,
            "green": greenDie.GreenDie,
            "red": redDie.RedDie
        }
        return localizers[color]()