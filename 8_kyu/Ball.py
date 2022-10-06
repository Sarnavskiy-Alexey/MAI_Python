"""
Create a class Ball. Ball objects should accept one argument for "ball type" when instantiated.
If no arguments are given, ball objects should instantiate with a "ball type" of "regular."
"""


class Ball(object):
    """ class Ball """
    def __init__(self, s_type=""):
        """ constructor """
        self.ball_type = s_type if s_type != "" else "regular"


if __name__ == '__main__':
    print(Ball().ball_type)
    print(Ball("super").ball_type)
