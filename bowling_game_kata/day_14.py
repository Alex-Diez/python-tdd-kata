import unittest


class BowlingGame(object):
    def __init__(self):
        self._rolls = []

    def roll(self, pin):
        self._rolls.append(pin)

    def score(self):
        score = 0
        frame_index = 0

        for _ in range(10):
            if self._is_strike(frame_index):
                score += 10 + self._strike_bonus(frame_index)
                frame_index += 1
            elif self._is_spare(frame_index):
                score += 10 + self._spare_bonus(frame_index)
                frame_index += 2
            else:
                score += self._rolls[frame_index] + self._rolls[frame_index + 1]
                frame_index += 2

        return score

    def _is_strike(self, frame_index):
        return self._rolls[frame_index] == 10

    def _strike_bonus(self, frame_index):
        return self._rolls[frame_index + 1] + self._rolls[frame_index + 2]

    def _is_spare(self, frame_index):
        return self._rolls[frame_index] + self._rolls[frame_index + 1] == 10

    def _spare_bonus(self, frame_index):
        return self._rolls[frame_index + 2]


class BowlingGameTest(unittest.TestCase):
    def setUp(self):
        self.game = BowlingGame()

    def _roll_many(self, times, pin):
        for _ in range(times):
            self.game.roll(pin)

    def _roll_spare(self):
        self.game.roll(4)
        self.game.roll(6)

    def _roll_strike(self):
        self.game.roll(10)

    def testGutterGame(self):
        self._roll_many(20, 0)

        self.assertEqual(0, self.game.score())

    def testAllOnes(self):
        self._roll_many(20, 1)

        self.assertEqual(20, self.game.score())

    def testOneSpare(self):
        self._roll_spare()
        self.game.roll(3)
        self._roll_many(17, 0)

        self.assertEqual(16, self.game.score())

    def testOneStrike(self):
        self._roll_strike()
        self.game.roll(4)
        self.game.roll(3)
        self._roll_many(16, 0)

        self.assertEqual(24, self.game.score())

    def testPerfectGame(self):
        self._roll_many(13, 10)

        self.assertEqual(300, self.game.score())
