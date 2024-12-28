from View.AddLinkScreen.add_link_screen import AddLinkScreenView


class AddLinkScreenController:
    """
    The `AddLinkScreenController` class represents a controller implementation.
    Coordinates work of the view with the model.
    The controller implements the strategy pattern. The controller connects to
    the view to control its actions.
    """

    def __init__(self, model):
        self.model = model  # Model.add_link_screen.AddLinkScreenModel
        self.view = AddLinkScreenView(controller=self, model=self.model)

    def get_view(self) -> AddLinkScreenView:
        return self.view

    def move_back_home(self):
        self.view.parent.current = 'home screen'
