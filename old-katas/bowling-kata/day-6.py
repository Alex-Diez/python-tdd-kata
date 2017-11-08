# -*- coding: utf-8 -*-

class Game(object):
    def __init__(self):
        self.rolls = []

    def roll(self, pins):
        self.rolls.append(pins)

    def score(self):
        score = 0
        frame_index = 0
        for i in range(0, 10):
            if self._is_strike(frame_index):
                score += self._strike_points(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += self._spare_points(frame_index)
                frame_index += 2
            else:
                score += self._frame_points(frame_index)
                frame_index += 2
        return score

    def _strike_points(self, frame_index):
        return 10 + self.rolls[frame_index + 1] + self.rolls[frame_index + 2]

    def _frame_points(self, frame_index):
        return self.rolls[frame_index] + self.rolls[frame_index + 1]

    def _spare_points(self, frame_index):
        return 10 + self.rolls[frame_index + 2]

    def _is_spare(self, frame_index):
        return self._frame_points(frame_index) == 10

    def _is_strike(self, frame_index):
        return self.rolls[frame_index] == 10


import unittest


class GameTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_gutter_game(self):
        self._roll_many(0, 20)
        self.assertEqual(0, self.game.score())

    def test_all_ones(self):
        self._roll_many(1, 20)
        self.assertEqual(20, self.game.score())

    def test_one_spare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(0, 17)
        self.assertEqual(16, self.game.score())

    def test_one_strike(self):
        self._roll_strike()
        self.game.roll(4)
        self.game.roll(3)
        self._roll_many(0, 16)
        self.assertEqual(24, self.game.score())

    def test_perfect_game(self):
        self._roll_many(10, 12)
        self.assertEqual(300, self.game.score())

    def _roll_strike(self):
        self.game.roll(10)

    def _roll_spare(self):
        self.game.roll(6)
        self.game.roll(4)

    def _roll_many(self, pins, times):
        for i in range(0, times):
            self.game.roll(pins)
