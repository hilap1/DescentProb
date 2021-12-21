import die
import die_face
import itertools
import numpy as np


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
    blue_die = die.Die('blue')
    red_die = die.Die('red')
    yellow_die = die.Die('yellow')
    green_die = die.Die('green')
    red_die.to_string()

    hearts_results = []
    serges_results = []
    range_result = []

    first_die = blue_die
    second_die = yellow_die

    dice_list = [blue_die, yellow_die, green_die]

    for i in itertools.combinations_with_replacement(range(0,6), len(dice_list)):

        dice_results = add_dice_results_list(create_possible_dice_result_list(dice_list, i))
        print("2 Dice add result " + dice_results.to_string())

        hearts_results.append(dice_results.hearts)
        serges_results.append(dice_results.surge)
        range_result.append(dice_results.range)

    print(np.average(hearts_results))
    print(np.average(serges_results))
    print(np.average(range_result))

    unique, counts = np.unique(hearts_results, return_counts=True)
    print(np.asarray((unique, counts)).T)

    unique, counts = np.unique(serges_results, return_counts=True)
    print(np.asarray((unique, counts)).T)

    unique, counts = np.unique(range_result, return_counts=True)
    print(np.asarray((unique, counts)).T)




