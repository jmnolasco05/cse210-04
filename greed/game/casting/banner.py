from game.casting.actor import Actor


class Banner(Actor):
    """A representation of the banner with the score
    """

    def __init__(self):
        super().__init__()
        self._score = 0

    def set_points(self, points):
        """Set the pointes earned.

        Args:
            points (_type_): _description_
        """
        self._score += points
        self._text = f"Score: {self._score}"
