class Shape:
    """Base class so all shapes have a draw() method."""

    def draw(self):
        raise NotImplementedError("Shape classes must implement draw().")

    def draw_solid(self):
        raise NotImplementedError("Shape classes must implement draw_solid().")

    def draw_edges(self):
        raise NotImplementedError("Shape classes must implement draw_edges().")
