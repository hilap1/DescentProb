import die
import die_face
import itertools
import numpy as np
import yellowDie


def check_if_result_is_x(die_result):
    if die_result.range == 0 and die_result.surge == 0 and die_result.hearts == 0:
        return True
    return False


def add_dice_results_list(dice_result_list):
    result = die_face.DieFace(0,0,0)
    for res in dice_result_list:
        if check_if_result_is_x(res):
            return result

    for res in dice_result_list:
        result.range = result.range + res.range
        result.surge = result.surge + res.surge
        result.hearts = result.hearts + res.hearts
    return result


def create_possible_dice_result_list(dice_list, combo):
    possible_dice_result_list = []
    for index in range(0,len(dice_list)):
        possible_dice_result_list.append(dice_list[index].faces[combo[index]])
    return possible_dice_result_list


if __name__ == '__main__':

    diedie = die.Die()
    yellow_die = diedie.factory("yellow")
    blue_die = diedie.factory("blue")
    green_die = diedie.factory("green")
    red_die = diedie.factory("red")

    hearts_results = []
    serges_results = []
    range_result = []

    dice_list = [blue_die, yellow_die, yellow_die]

    for item in itertools.product(blue_die.faces, yellow_die.faces , yellow_die.faces):
        dice_results = add_dice_results_list(item)

        hearts_results.append(dice_results.hearts)
        serges_results.append(dice_results.surge)
        range_result.append(dice_results.range)









