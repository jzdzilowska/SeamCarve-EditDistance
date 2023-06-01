import pytest

from edits import edit_distance_bwd, edit_distance_fwd
from seamcarve import SeamCarve

def test_edits():
    # TODO: add more test functions with assertions on edit_distance_fwd 
    # and edit_distance_bwd based on examples you've seen or make yourself

    # tests below check multiple cases for edit distance calculation - transforming empty strings into words
    # and words into empty strings, preserving empty strings, preserving words, ignoring capitalization, 
    # transforming words with the same lengths but different characters (all of them different,
    # or only a few of them / just one different), the same characters but different 
    # lengths, different characters and different lenghts, adding new characters, adding the same characters, 
    # removing characters, making changes to the beginning, middle, or the end of the word. 
    # I approached creating these tests systematically, to ensure that various different cases 
    # are taken into account to reveal the potential bugs. Neither the first nor the second version are working
    # (although they fail for different reasons).

    assert edit_distance_fwd("", "") == 0
    assert edit_distance_fwd("", "word") == 4
    assert edit_distance_fwd("word", "") == 4
    assert edit_distance_fwd("word", "word") == 0
    assert edit_distance_fwd("Word", "word") == 0 
    assert edit_distance_fwd("word", "Word") == 0 
    assert edit_distance_fwd("oneword", "twoword") == 3
    assert edit_distance_fwd("espresso", "expresso") == 1 
    assert edit_distance_fwd("apples", "accent") == 5
    assert edit_distance_fwd("apples", "iconic") == 6
    assert edit_distance_fwd("espresso", "espeross") == 3 
    assert edit_distance_fwd("espresso", "esperos") == 4 
    assert (edit_distance_fwd("word", "twoword") == edit_distance_fwd("oneword", "word") == 3)
    assert (edit_distance_fwd("wordone", "wordtwa")) == 3
    assert (edit_distance_fwd("wordone", "wordonetwothree")) == 8

    assert edit_distance_bwd("", "") == 0
    assert edit_distance_bwd("", "word") == 4
    assert edit_distance_bwd("word", "") == 4
    assert edit_distance_bwd("word", "word") == 0
    assert edit_distance_bwd("Word", "word") == 0 
    assert edit_distance_bwd("word", "Word") == 0 
    assert edit_distance_bwd("oneword", "twoword") == 3
    assert edit_distance_bwd("espresso", "expresso") == 1 
    assert edit_distance_bwd("apples", "accent") == 5
    assert edit_distance_bwd("apples", "iconic") == 6
    assert edit_distance_bwd("espresso", "espeross") == 3 
    assert (edit_distance_bwd("espresso", "espeross") != edit_distance_bwd("espresso", "esperos"))
    assert (edit_distance_bwd("word", "twoword") == edit_distance_fwd("oneword", "word") == 3)
    assert (edit_distance_bwd("wordone", "wordtwa")) == 3
    assert (edit_distance_bwd("wordone", "wordonetwothree")) == 8

def test_argmin():
    test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
        [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
        [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
        [255, 255, 255]]]
    
    seam_carve = SeamCarve(image_matrix = test_image)
    test_row = [2, 3, 10, 0]
    zero_row = [0, 0, 0, 0]
    same_row = [1, 1, 1, 1]
    duplicates_row = [0, 1, 1, 10]
    neg_row = [0, -100, -22, 10]
    assert seam_carve.argmin(test_row) == 3
    assert seam_carve.argmin(zero_row) == 0
    assert seam_carve.argmin(same_row) == 0
    assert seam_carve.argmin(duplicates_row) == 0
    assert seam_carve.argmin(neg_row) == 1



def test_seamcarve():
    # TODO: add more assertions and/or test functions to test seamcarve
    # cell E1 from 5x5 spreadsheet
    test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
        [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
        [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
        [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
        [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
        [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
        [255, 255, 255]]]
    expected_seam1 = [2, 1, 1, 2, 3]
    my_sc = SeamCarve(image_matrix = test_image)
    importance_vals1 = my_sc.calculate_importance_values()
    calculated_seam1 = my_sc.find_least_important_seam(importance_vals1)
    assert expected_seam1 == calculated_seam1


    test_image_diagonal_gap = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],\
                            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
                            [[255, 255, 255], [255, 255, 255], [0, 0, 0], [255, 255, 255], [255, 255, 255]], 
                            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
                            [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    expected_seam2 = [1, 2, 2, 2, 1]
    my_sc2 = SeamCarve(image_matrix = test_image_all_same)
    importance_vals2 = my_sc2.calculate_importance_values()
    calculated_seam2 = my_sc2.find_least_important_seam(importance_vals2)
    assert expected_seam2 == calculated_seam2

    test_image_one_diagonal = [[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]],\
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
        [[255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255], [255, 255, 255]], 
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]], 
        [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]]
    expected_seam3 = [0, 1, 1, 1, 0]
    my_sc3 = SeamCarve(image_matrix = test_image_one_diagonal)
    importance_vals3 = my_sc3.calculate_importance_values()
    calculated_seam3 = my_sc3.find_least_important_seam(importance_vals3)
    assert expected_seam3 == calculated_seam3

    test_image_one_checkerboard = [[[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]],\
                                   [[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]], 
                                   [[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]], 
                                   [[255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255]], 
                                   [[0, 0, 0], [255, 255, 255], [0, 0, 0], [255, 255, 255], [0, 0, 0]]]
    expected_seam4 = [0, 0, 0, 0, 0]
    my_sc4 = SeamCarve(image_matrix = test_image_one_checkerboard)
    importance_vals4 = my_sc4.calculate_importance_values()
    calculated_seam4 = my_sc4.find_least_important_seam(importance_vals4)
    assert expected_seam4 == calculated_seam4
    # test_image = [[[255, 255, 255], [0, 0, 0], [125, 125, 125], [0, 0, 0],\
    #     [255, 255, 255]], [[0, 0, 0], [125, 125, 125], [0, 0, 0],
    #     [255, 255, 255], [0, 0, 0]], [[255, 255, 255], [125, 125, 125],
    #     [255, 255, 255], [0, 0, 0], [255, 255, 255]], [[0, 0, 0],
    #     [255, 255, 255], [125, 125, 125], [255, 255, 255], [0, 0, 0]], 
    #     [[255, 255, 255], [0, 0, 0], [255, 255, 255], [125, 125, 125],
    #     [255, 255, 255]]]

    # my_sc = SeamCarve(image_matrix = test_image)
    # calculated_seam = my_sc.find_least_important_seam([[3,6,8],[5,7,2],[4,9,3]])
    # expected_seam = [1,2,2]
    # assert expected_seam == calculated_seam

