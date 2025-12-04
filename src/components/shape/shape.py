class Shape:
    """Base class so all shapes have a draw() method."""

    def draw(self):
        raise NotImplementedError("Shape classes must implement draw().")
