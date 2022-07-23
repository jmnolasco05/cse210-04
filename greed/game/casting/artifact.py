from game.casting.actor import Actor


class Artifact(Actor):
    """
    An gem or a rock. 

    The responsibility of an Artifact is to add or substract points for the score.

    Attributes:
        _points (int): Points earned with this artifact.
    """

    def __init__(self):
        super().__init__()
        self._points = 0

    def get_points(self):
        """Gets the artifact's message.

        Returns:
            string: The message.
        """
        return self._points

    def set_points(self, points):
        """Updates the points to the given one.

        Args:
            point (int): The given points.
        """
        self._points = points
