"""
    Reference: https://www.codewars.com//kata/53f0f358b9cb376eca001079
"""


class Ball(object):
    """ class Ball """
    def __init__(self, s_type=""):
        """ constructor """
        self.ball_type = s_type if s_type != "" else "regular"


if __name__ == '__main__':
    print(Ball().ball_type)
    print(Ball("super").ball_type)
